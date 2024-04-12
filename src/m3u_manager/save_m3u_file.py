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
    visited_links = set()  # Set to store visited links

    with open(url_name, 'w+') as f:
        f.write("#EXTM3U\n\n")  # Removed url_name from #EXTM3U tag
        for channel_info, link in ext_inf:
            # Check if the link has been visited already
            if link in visited_links:
                continue  # If it's a duplicate link, move to the next channel
            else:
                visited_links.add(link)  # Add the link to the set of visited links

            # Extract parsed values if available
            parsed_values = {}
            if any(key in channel_info for key in dict_m3u.keys()):
                channel_info_modified = add_symbol(channel_info)
                parsed_values = extract_values(channel_info_modified, dict_m3u)

            # Write channel information
            if parsed_values:  # If parsed_values exist, write EXTINF with parsed values
                extinf_values = ''.join(
                    [
                        f'{key}={value.upper()}' if key.lower() == 'group-title' else f'{key}={value}' if ' ' in value else f'{key}="{value}"'
                        for key, value in parsed_values.items()])
                f.write(f"#EXTINF:{extinf_values}\n")

            else:  # If parsed_values do not exist, write channel_info as is
                f.write(f"{channel_info}\n")  # Convert channel_info to uppercase before writing
            # Write the link
            f.write(f"{link}\n\n")  # Add newline after each channel
