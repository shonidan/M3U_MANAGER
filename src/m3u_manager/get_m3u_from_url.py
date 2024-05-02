import logging
import requests
from urllib.parse import urlparse, parse_qs

def parse_url(url):
    parsed_url = urlparse(url)
    query_string = parsed_url.query
    parsed_query_string = parse_qs(query_string)
    return parsed_query_string

def process_url(url):
    params = parse_url(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36'
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        content = response.text
        return content
    else:
        print("Error:", response.status_code)
        return None


def get_m3u_from_url(url):
    try:
        # New code added
        content = ""  # Inicializamos content como una cadena vacía
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logging.info("URL Available")
                content = response.text  # Guarda el contenido de la respuesta exitosa
            elif response.status_code == 403:
                logging.info("Access Forbidden. Processing URL...")
                processed_content = process_url(url)
                if processed_content:
                    content += processed_content  # Agrega el contenido procesado al contenido original
            else:
                logging.info(f"{url} is not reachable (Status Code: {response.status_code}).")
                with open("error_urls.txt", "a") as f:
                    f.write(f"{url} (Status Code: {response.status_code})\n")
        except requests.ConnectionError:
            print(f"{url} is not reachable.")
            with open("error_urls.txt", "a") as f:
                f.write(f"{url} (Connection Error)\n")
        # End of new code

        # Si la solicitud fue exitosa, lee el contenido de la respuesta
        response.raise_for_status()  # Verifica errores en la respuesta

        # Si la respuesta fue exitosa, lee el contenido de la respuesta
        content = response.text.splitlines()

        # Lista para almacenar nombres de canal y enlaces m3u/m3u8
        channel_names_and_url = []

        # Itera sobre cada línea y busca enlaces HTTP y HTTPS o que terminen con .m3u y .m3u8
        for i, line in enumerate(content):
            if line.strip().startswith(('https://', 'http://')) or line.strip().endswith(('.m3u', '.m3u8')):
                # Obtiene el nombre del canal (línea anterior) si existe
                if i > 0:
                    channel_info = content[i - 1]
                else:
                    channel_info = None

                # Agrega el nombre del canal y el enlace a la lista
                channel_names_and_url.append((channel_info, line.strip()))

        return channel_names_and_url

    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return []