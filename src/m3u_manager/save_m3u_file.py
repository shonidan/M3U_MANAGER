from src.utils.metadata_m3u import dict_m3u

def add_symbol(channel_info):
    # Agregar el símbolo ∭ antes de cada clave
    modified_info = ""
    for word in channel_info.split():
        if '=' in word:
            key, value = word.split('=', 1)  # Dividir solo una vez
            modified_info += f" ∭{key}={value}"
        else:
            modified_info += f" {word}"
    # Agregar el símbolo ∭ al final
    modified_info += " ∭"
    return modified_info.strip()

def extract_values(channel_info, metadata_dict):
    parsed_values = {}

    # Encuentra el índice de inicio de cada clave en el channel_info
    start_indexes = [channel_info.find(f'∭{key}=') for key in metadata_dict.keys()]

    # Recorre cada índice de inicio
    for start_index, (key, value) in zip(start_indexes, metadata_dict.items()):
        if start_index != -1:
            # Encuentra el índice de fin de cada clave
            end_index = channel_info.find("∭", start_index + 1)
            if end_index != -1:
                # Extrae el contenido entre el símbolo = y ∭
                start_value_index = start_index + len(key) + 2  # Índice después del símbolo =
                extracted_value = channel_info[start_value_index:end_index]

                # Actualiza los valores extraídos
                parsed_values[key] = extracted_value

    return parsed_values

def save_file_in_m3u(ext_inf, url_name):
    visited_links = set()  # Set para almacenar enlaces visitados

    with open(url_name, 'w+') as f:
        f.write("#EXTM3U\n\n")  # Escribir la etiqueta inicial

        for channel_info, link in ext_inf:
            # Verificar si el enlace ya se ha visitado
            if link in visited_links:
                continue  # Si es un enlace duplicado, pasa al siguiente canal
            else:
                visited_links.add(link)  # Añadir el enlace al conjunto de enlaces visitados

            # Extraer valores analizados si están disponibles
            parsed_values = {}
            if any(key in channel_info for key in dict_m3u.keys()):
                channel_info_modified = add_symbol(channel_info)
                parsed_values = extract_values(channel_info_modified, dict_m3u)

                # Verificar si 'tvg-logo' existe y si su valor no empieza con 'http'
                if 'tvg-logo' in parsed_values:
                    tvg_logo_value = parsed_values['tvg-logo']
                    if not tvg_logo_value.startswith('http'):
                        # Si 'tvg-logo' no empieza con 'http', vaciar el valor entre comillas
                        parsed_values['tvg-logo'] = ''

            # Escribir la información del canal
            if parsed_values:  # Si existen valores analizados, escribir EXTINF con los valores analizados
                extinf_values = ''.join(
                    [
                        f'{key}={value}' if ' ' in value else f'{key}="{value}"'
                        for key, value in parsed_values.items()
                    ]
                )
                f.write(f"#EXTINF:{extinf_values}\n")

            else:  # Si no existen valores analizados, escribir channel_info tal como está
                f.write(f"{channel_info.upper()}\n")  # Convertir channel_info a mayúsculas antes de escribir

            # Escribir el enlace
            f.write(f"{link}\n\n")  # Añadir nueva línea después de cada canal
