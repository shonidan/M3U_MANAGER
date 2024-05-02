from src.utils.metadata_m3u import dict_m3u


def add_symbol(channel_info):
    # Add the symbol ∭ before each key
    modified_info = ""
    for word in channel_info.split():
        if '=' in word:
            key, value = word.split('=', 1)  # Split only once
            modified_info += f" ∭{key}={value}"
        else:
            modified_info += f" {word}"
    # Add the symbol ∭ at the end
    modified_info += " ∭"
    return modified_info.strip()


def extract_values(channel_info, metadata_dict):
    parsed_values = {}

    # Find the start index of each key in the channel_info
    start_indexes = [channel_info.find(f'∭{key}=') for key in metadata_dict.keys()]

    # Iterate through each start index
    for start_index, (key, value) in zip(start_indexes, metadata_dict.items()):
        if start_index != -1:
            # Find the end index of each key
            end_index = channel_info.find("∭", start_index + 1)
            if end_index != -1:
                # Extract the content between the = symbol and ∭
                start_value_index = start_index + len(key) + 2  # Index after the = symbol
                extracted_value = channel_info[start_value_index:end_index]

                # If the key is "tvg-name", remove anything after the last quotation mark
                if key == "tvg-name" and '"' in extracted_value:
                    last_quote_index = extracted_value.rfind('"')
                    extracted_value = extracted_value[:last_quote_index + 1]  # Keep the last quotation mark

                # Update the extracted values
                parsed_values[key] = extracted_value

    return parsed_values


def save_file_in_m3u(ext_inf, url_name):
    visited_links = set()  # Set to store visited links

    with open(url_name, 'w+', encoding='utf-8') as f:
        f.write("#EXTM3U\n\n")  # Removed url_name from #EXTM3U tag
        for channel_info, link in ext_inf:
            # Convertir el nombre del grupo a mayúsculas
            channel_group_upper = url_name.upper().replace(".M3U", "")
            # Verificar si el enlace ya ha sido visitado
            if link in visited_links:
                continue  # If it's a duplicate link, move to the next channel
            else:
                visited_links.add(link)  # Add the link to the set of visited links

            # Extract parsed values if available
            parsed_values = {}
            if any(key in channel_info for key in dict_m3u.keys()):
                channel_info_modified = add_symbol(channel_info)
                parsed_values = extract_values(channel_info_modified, dict_m3u)

            # Agregar lógica para insertar group-title si no se encuentra en la información del canal
            if "group-title" not in channel_info:
                channel_info = f"#EXTINF: group-title=\"{channel_group_upper}\"" + channel_info

            # Escribir información del canal
            if parsed_values:
                extinf_values = ''.join(
                    [
                        f'{key}={value.upper()}' if key.lower() == 'group-title' else f'{key}={value}' if ' ' in value else f'{key}="{value}"'
                        for key, value in parsed_values.items()])
                f.write(f"#EXTINF:{extinf_values}\n")

            else:  # If parsed_values do not exist, write channel_info as is
                f.write(f"{channel_info}\n")  # Convert channel_info to uppercase before writing
            # Write the link
            f.write(f"{link}\n\n")  # Add newline after each channel
