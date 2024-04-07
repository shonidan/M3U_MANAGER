from src.utils.metadata_m3u import dict_m3u


def extract_values(channel_name, metadata_dict):
    parsed_values = {}
    keys = list(metadata_dict.keys())

    # Split the channel_name into lines
    lines = channel_name.strip().split('\n')

    for key in keys:
        for line in reversed(lines):
            key_index = line.find(f'{key}="')
            if key_index != -1:
                # Start search after key
                start_index = key_index + len(key) + 2

                # Find the next occurrence of the next key or end of line
                next_key = keys[keys.index(key) + 1] if key_index < len(keys) - 1 else None
                next_key_index = len(line) if next_key is None else line.find(f'{next_key}="', start_index)

                # Extracting value between start_index and next_key_index
                value = line[start_index:next_key_index].strip('"')

                # Check if this is the first key
                if not parsed_values:
                    parsed_values[key] = value
                else:
                    # Add key-value pair with comma separation
                    if key in parsed_values:
                        parsed_values[key] += f", {value}"
                    else:
                        parsed_values[key] = value

                # Update lines to consider only the lines before this line
                lines = lines[:lines.index(line)]
                break

    return {k: v for k, v in parsed_values.items() if k in metadata_dict}


def save_file_in_m3u(ext_inf, url_name):
    visited_links = set()  # Set to store visited links

    with open(url_name, 'w') as f:
        f.write("#EXTM3U-" + url_name + "\n\n")
        for channel_name, link in ext_inf:
            # Check if the link has been visited already
            if link in visited_links:
                continue  # If it's a duplicate link, move to the next channel
            else:
                visited_links.add(link)  # Add the link to the set of visited links

            parsed_values = extract_values(channel_name, dict_m3u)
            if parsed_values:
                f.write("#EXTINF:")
                for key, value in parsed_values.items():
                    f.write(f"{key}=\"{value}\" ")
            else:
                f.write(channel_name)  # If no keys are found, write the channel_name directly
            f.write(f"\n{link}\n\n")
