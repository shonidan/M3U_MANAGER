import json
import re


def remove_channels_from_json(json_file, substrings):
    """
    Removes channels from the JSON file based on the specified substrings.

    Args:
        json_file (str): Path to the JSON file.
        substrings (list): List of substrings to search for in group names.
    """
    # Open the JSON file and load its content into a dictionary
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Iterate over the dictionary keys
    keys_to_remove = []

    for key in data:
        # Check if any of the substrings match the key
        for substring in substrings:
            if substring.lower() in key.lower():
                keys_to_remove.append(key)
                break  # No need to check further once a match is found

        # Check if any of the channels within the group match the substrings
        channels_to_remove = []

        for channel in data[key]:
            for substring in substrings:
                if substring.lower() in channel['info'].lower() or substring.lower() in channel['url'].lower():
                    channels_to_remove.append(channel)
                    break  # No need to check further once a match is found

        # Remove the channels from the group
        for channel in channels_to_remove:
            data[key].remove(channel)

    # Remove the keys and their associated channels
    for key in keys_to_remove:
        del data[key]

    # Write the updated dictionary back to the JSON file
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
