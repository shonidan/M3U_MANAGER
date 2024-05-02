import json


def json_to_m3u(json_file):
    json_name = json_file.replace(".json", "")
    with open(json_file, 'r', encoding='utf-8') as json_data:
        data = json.load(json_data)

    with open(f"{json_name}.m3u", 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n\n")  # Write the m3u file header
        for channel_group, channels_info in data.items():
            for channel_data in channels_info:
                info = channel_data.get("info", "")
                url = channel_data.get("url", "")
                if info and url:  # Check if both values exist
                    f.write(f"{info}\n")  # Write channel information
                    f.write(f"{url}\n")  # Write the URL
                    f.write("\n")  # Add a newline after each URL
