import json


def json_to_m3u(json_file):
    json_name = json_file.replace(".json", "")
    with open(json_file, "r") as json_data:
        data = json.load(json_data)

    with open(f"{json_name}.m3u", "w") as f:
        f.write("#EXTM3U\n\n")  # Write the m3u file header
        for channel_group, channels_info in data.items():
            # Convertir el nombre del grupo a mayúsculas
            channel_group_upper = channel_group.upper()

            for channel_data in channels_info:
                info = channel_data.get("info", "")
                url = channel_data.get("url", "")

                # Add logic to insert group-title if not found in info
                if "group-title" not in info:
                    # Find the index of #EXTINF: and insert group-title after it
                    extinf_index = info.find("#EXTINF:")
                    if extinf_index != -1:
                        info = info[
                               :extinf_index + len("#EXTINF:")] + f" group-title=\"{channel_group_upper}\" " + info[
                                                                                                               extinf_index + len(
                                                                                                                   "#EXTINF:"):]
                    else:
                        info = f"#EXTINF: group-title=\"{channel_group_upper}\"" + info

                if info and url:  # Check if both values exist
                    f.write(f"{info}\n")  # Write channel information
                    f.write(f"{url}\n")  # Write the URL
                    f.write("\n")  # Add a newline after each URL
