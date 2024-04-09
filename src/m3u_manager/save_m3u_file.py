from src.utils.metadata_m3u import dict_m3u


def extract_values(channel_name, metadata_dict):
    parsed_values = {}

    # Iterate over each key in the metadata dictionary
    for key, value in metadata_dict.items():
        # Find the start and end positions of the key in the channel_name
        start_index = channel_name.find(f'{key}="')
        if start_index != -1:
            start_index += len(key) + 2  # Move to the character after the key's opening quotes
            end_index = channel_name.find('"', start_index)  # Find the closing quotes

            # Extract the content between the quotes
            extracted_value = channel_name[start_index:end_index]

            # Update parsed values
            parsed_values[key] = extracted_value

    return parsed_values


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


