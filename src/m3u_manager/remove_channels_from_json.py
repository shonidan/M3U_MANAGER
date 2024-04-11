import json


def remove_channels_from_json(json_file, substrings, exceptions=None):
    """
    Removes channels from the JSON file based on the specified substrings and exceptions.

    Args:
        json_file (str): Path to the JSON file.
        substrings (list): List of substrings to search for in group names and channel info.
        exceptions (list, optional): List of substrings to exclude from removal.
    """
    # Load the JSON data from the file
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Initialize a list to track keys to remove
    keys_to_remove = []

    # Iterate through the groups in the JSON data
    for key in data:
        # Check if any substring matches the group name
        if any(substring.lower() in key.lower() for substring in substrings):
            keys_to_remove.append(key)
            continue

        # Initialize a list to track channels to remove within the group
        channels_to_remove = []

        # Iterate through the channels in the current group
        for channel in data[key]:
            channel_info = channel['info'].lower()

            # Check if the channel should be excluded based on exceptions
            if exceptions and any(exc.lower() in channel_info for exc in exceptions):
                continue  # Skip this channel and proceed to the next one

            # Check if any substring matches the channel info
            if any(substring.lower() in channel_info for substring in substrings):
                channels_to_remove.append(channel)

        # Remove channels marked for removal from the group
        for channel in channels_to_remove:
            data[key].remove(channel)

    # Remove groups marked for removal
    for key in keys_to_remove:
        del data[key]

    # Write the updated data back to the JSON file
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def keep_channels_with_substrings(json_file, substrings):
    """
    Keeps channels containing any of the specified substrings in their info or url fields.

    Args:
        json_file (str): Path to the JSON file.
        substrings (list): List of substrings to search for in channel info or url fields.
    """
    # Open the JSON file and load its content into a dictionary
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Iterate over the dictionary keys
    keys_to_keep = []

    for key in data:
        # Check if any of the channels within the group match the substrings
        channels_to_keep = []

        for channel in data[key]:
            for substring in substrings:
                if substring.lower() in channel['info'].lower() or substring.lower() in channel['url'].lower():
                    channels_to_keep.append(channel)
                    break  # No need to check further once a match is found

        # Remove channels not containing any of the substrings
        data[key] = channels_to_keep
        if channels_to_keep:
            keys_to_keep.append(key)

    # Remove keys without any channels to keep
    for key in list(data.keys()):
        if key not in keys_to_keep:
            del data[key]

    # Write the updated dictionary back to the JSON file
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)