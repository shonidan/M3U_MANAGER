from src.utils.metadata_m3u import dict_m3u


def extract_values(channel_name, metadata_dict):
    parsed_values = {}
    keys = list(metadata_dict.keys())

    # Split the channel_name into lines
    lines = channel_name.strip().split('\n')

    for key in keys:
        for line in lines:
            key_index = line.find(f'{key}="')
            if key_index != -1:
                # Start search after key
                start_index = key_index + len(key) + 2

                # Find the end of value (next double quote)
                end_index = line.find('"', start_index)

                # Check if it's group-title key
                if key == 'group-title':
                    # If it's group-title, find the end of value until the second double quote
                    end_index = line.find('"', end_index + 1)

                # Extract value
                value = line[start_index:end_index].strip('"')

                # Convert group-title value to uppercase
                if key == 'group-title':
                    value = value.upper()

                # Update parsed values
                parsed_values[key] = value
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
                f.write(channel_name.upper())  # Convert channel_name to uppercase
            f.write(f"\n{link}\n\n")


