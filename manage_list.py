import json
from src.m3u_manager.iptv_checker import teststream_json
from src.m3u_manager.list_key_json import list_key_names
from src.m3u_manager.get_m3u_from_url import get_m3u_from_url
from src.m3u_manager.json_to_m3u import json_to_m3u
from src.m3u_manager.m3u_to_json import merge_m3u_to_json
from src.m3u_manager.remove_channels_from_json import remove_channels_from_json, keep_channels_with_substrings
from src.m3u_manager.remove_duplicates_url import remove_duplicate_urls
from src.m3u_manager.save_m3u_file import save_file_in_m3u
from src.utils.metadata_m3u import topics_nsfw, ignore_similar_topics


def get_all_m3u_from_url(url):
    """
    Steps to manage one or more URLs:
    1 - Retrieve all M3U playlists from the given URL(s), checking the status code for each URL (get_m3u_from_url).
    2 - Merge all M3U playlists into a JSON file.
    3 - (Optional) Remove channels by topic in the JSON.
    4 - (Optional) Keep channels by topic in the JSON.
    5 - List group titles for display.
    6 - Convert all channels from JSON to M3U format.
    7 - Experimental: Check online channels and remove offline channels.
    """
    # Step 1
    m3u_list = get_m3u_from_url(url)

    # Step 2
    ext_inf = remove_duplicate_urls(m3u_list)

    # Step 3
    save_file_in_m3u(ext_inf, f"{url_name}.m3u")  # Changed variable_name to url


# Load the JSON file.
with open('src/utils/URLS.json', 'r') as file:
    urls = json.load(file)
# Iterate over each item in the JSON and execute get_all_m3u_from_url with the corresponding value.
for url_name, url_value in urls.items():
    print(f"Executing get_all_m3u_from_url for {url_name}: {url_value}")
    get_all_m3u_from_url(url_value)

# Step 4
merge_m3u_to_json()

# Step optional: Delete NSFW content.
topics_to_delete = topics_nsfw
ignore_similar_topics = ignore_similar_topics
# remove_channels_from_json("ALL_CHANNELS.json", topics_to_delete, ignore_similar_topics)

# Step optional: Keep only specified topics.
topics_to_keep = topics_nsfw
# keep_channels_with_substrings("ALL_CHANNELS.json", topics_to_keep)

# Step 5
list_key_names("ALL_CHANNELS.json")

# Step 6
json_to_m3u("ALL_CHANNELS.json")

# Step 7: Optional. Activate this option to check available channels. This process may take a significant amount of time.
# teststream_json("ALL_CHANNELS.json")
