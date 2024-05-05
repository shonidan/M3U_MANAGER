import os
import subprocess
from PIL import Image
import pytesseract
import json
from urllib.parse import urlparse

# Función para realizar OCR en una imagen y determinar si contiene la palabra "error"
def ocr(image_path):
    # Capturar texto de la imagen utilizando Tesseract OCR
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Ubicación de tesseract en tu sistema
    text = pytesseract.image_to_string(Image.open(image_path))

    # Verificar si la palabra "error" está presente en el texto
    if "error" in text.lower():
        return False
    else:
        return True

    # Eliminar el archivo 'stream.mp4' si existe
    if os.path.exists('stream.mp4'):
        os.remove('stream.mp4')

# Función para descargar y verificar una transmisión
def teststream(url):
    try:
        # Descargar la transmisión durante el tiempo especificado
        subprocess.run(['ffmpeg', '-t', '5', '-i', url, '-vsync', '0', '-acodec', 'copy', '-vcodec', 'copy', '-tls_verify', '0', 'stream.mp4'])

        # Invocar OCR en un fotograma de la transmisión descargada
        if not ocr('frame.jpg'):  # Suponiendo que 'frame.jpg' es el nombre del archivo de imagen del fotograma
            return False

        # Verificar el tamaño del archivo descargado
        file_size = os.path.getsize('stream.mp4')

        # Si el tamaño es menor o igual a 500 bytes, la transmisión se considera no válida
        if file_size <= 500:
            return False
        else:
            return True
    except:
        return False
    finally:
        # Eliminar el archivo 'stream.mp4' después de la última validación
        if os.path.exists('stream.mp4'):
            os.remove('stream.mp4')

# Función para verificar las transmisiones en un archivo JSON
def teststream_json(json_file):
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)

    valid_groups = {}  # Diccionario para almacenar grupos con al menos una URL válida

    for group_name, channels in data.items():
        online_urls = {}  # Diccionario para almacenar URLs en línea
        offline_urls = {}  # Diccionario para almacenar URLs sin conexión
        failed_server = None  # Variable para almacenar el dominio del servidor de la última URL que falló

        # Verificar cada canal en el grupo
        for channel in channels:
            url = channel['url']
            is_online = teststream(url)  # Verificar si la URL está en línea

            # Si la URL está en línea
            if is_online:
                parsed_url = urlparse(url)
                server = parsed_url.netloc

                # Verificar si la URL pertenece al mismo servidor que ya está en línea
                if any(urlparse(online_url).netloc == server for online_url in online_urls):
                    online_urls[url] = channel
                    continue

                online_urls[url] = channel
                failed_server = None  # Reiniciar la variable failed_server
            else:
                parsed_url = urlparse(url)
                server = parsed_url.netloc
                if failed_server and server == failed_server:
                    offline_urls[url] = channel
                else:
                    failed_server = server

        # Si hay al menos una URL en línea, guardar el grupo en el diccionario de grupos válidos
        if online_urls:
            valid_groups[group_name] = online_urls

    # Guardar el JSON resultante
    output_file = os.path.splitext(json_file)[0] + '_output.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(valid_groups, f, indent=4)

    # Convertir el JSON resultante a un archivo M3U
    json_to_m3u(output_file)

def json_to_m3u(json_file):
    json_name = json_file.replace(".json", "")
    with open(json_file, 'r', encoding='utf-8') as json_data:
        data = json.load(json_data)

    with open(f"{json_name}.m3u", 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n\n")  # Write the m3u file header
        for channel_group, channels_info in data.items():
            for channel_data in channels_info:
                info = channel_data.get("info", "")
                url = channel_data.get("url", "")
                if info and url:  # Check if both values exist
                    f.write(f"{info}\n")  # Write channel information
                    f.write(f"{url}\n")  # Write the URL
                    f.write("\n")  # Add a newline after each URL