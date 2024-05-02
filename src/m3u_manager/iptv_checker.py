import os
import subprocess
from PIL import Image
import pytesseract
import json

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

    # Iterar sobre cada grupo en el JSON
    for group_name, channels in data.items():
        for channel in channels:
            if not teststream(channel['url']):  # Si la transmisión no está en línea
                channels.remove(channel)  # Eliminar la entrada del canal

    # Guardar el JSON resultante
    output_file = os.path.splitext(json_file)[0] + '_output.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)