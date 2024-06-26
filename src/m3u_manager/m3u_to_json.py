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
        directory = os.getcwd()  # Use current directory if none provided

    merged_channels = {}
    urls_seen = set()

    # Extensions to ignore
    ignored_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.mkv', '.flv', '.mpg', '.mpeg', '.m4v', '.rm', '.rmvb',
                          '.3gp']

    for filename in os.listdir(directory):
        if filename.lower().endswith('.m3u'):  # Ignore case of file extension
            m3u_file = os.path.join(directory, filename)
            m3u_name = os.path.splitext(filename)[0]
            m3u_list = []

            with open(m3u_file, 'r', encoding='utf-8') as m3u:
                for line in m3u:
                    if line.startswith('#EXTINF'):
                        url = next(m3u).strip()  # Next line is the URL
                        if url not in urls_seen:  # Check if URL has been seen before
                            urls_seen.add(url)  # Add URL to seen URLs set
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

                    # Convert group name to uppercase, except for URL
                    if group_key != 'URL':
                        group_key = group_key.upper()

                # Replace #EXTINF:-1 with #EXTINF:
                info = tupla[0]

                # Check if any ignored extension is present in tupla[0] or tupla[1], if so, skip it
                if not any(extension.lower() in tupla[0].lower() or extension.lower() in tupla[1].lower()
                           for extension in ignored_extensions):
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

    # Remove .m3u files
    for filename in os.listdir(directory):
        if filename.lower().endswith('.m3u'):  # Modify to ignore case of extension
            os.remove(os.path.join(directory, filename))
