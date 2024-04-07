import json
import re
import os

def save_to_json(channels_dict, url_name):
    """
    Saves the dictionary of channels to a JSON file.

    Args:
        channels_dict (dict): Dictionary containing channel information.
        url_name (str): Name of the output JSON file.
    """
    with open(f'{url_name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(channels_dict, json_file, ensure_ascii=False, indent=4, sort_keys=True)

def merge_m3u_to_json(directory=None):
    if directory is None:
        directory = os.getcwd()  # Usa el directorio actual si no se proporciona ninguno

    merged_channels = {}

    for filename in os.listdir(directory):
        if filename.endswith('.m3u'):
            m3u_file = os.path.join(directory, filename)
            m3u_name = os.path.splitext(filename)[0]
            m3u_list = []

            with open(m3u_file, 'r', encoding='utf-8') as m3u:
                for line in m3u:
                    if line.startswith('#EXTINF'):
                        url = next(m3u).strip()  # Next line is the URL
                        m3u_list.append((line.strip(), url))

            channels_dict = {}

            for tupla in m3u_list:
                key_value = None

                # Search for group-title value using regular expression
                group_title_pattern = r'group-title="([^"]+)"'
                match = re.search(group_title_pattern, tupla[0])
                if match:
                    key_value = match.group(1).replace(' ', '_')

                if key_value is None:
                    # If group-title is not found, use m3u_name as the grouping key
                    group_key = m3u_name
                else:
                    # If group-title is found, use it as the grouping key
                    group_key = key_value

                # Replace #EXTINF:-1 with #EXTINF:
                info = tupla[0].replace("#EXTINF:-1", "#EXTINF:")

                # Check if the group already exists in the dictionary
                if group_key in channels_dict:
                    channels_dict[group_key].append({
                        'info': info,
                        'url': tupla[1]
                    })
                else:
                    channels_dict[group_key] = [{
                        'info': info,
                        'url': tupla[1]
                    }]

            merged_channels.update(channels_dict)

    save_to_json(merged_channels, 'ALL_CHANNELS')

    # Eliminar archivos .m3u
    for filename in os.listdir(directory):
        if filename.endswith('.m3u'):
            os.remove(os.path.join(directory, filename))
