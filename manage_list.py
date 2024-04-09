import json
from src.m3u_manager.list_key_json import list_key_names
from src.m3u_manager.get_m3u_from_url import get_m3u_from_url
from src.m3u_manager.json_to_m3u import json_to_m3u
from src.m3u_manager.m3u_to_json import merge_m3u_to_json
from src.m3u_manager.remove_channels_from_json import remove_channels_from_json
from src.m3u_manager.remove_duplicates_url import remove_duplicate_urls
from src.m3u_manager.save_m3u_file import save_file_in_m3u


def get_all_m3u_from_url(url):
    """
    Steps to manage url or more than one url
    1 - Get all m3u from url, checking status code from each url (get_m3u_from_url)
    2 - Remove duplicates m3u from URLS.json (remove_duplicates_url)
    3 - Save channels by info and alphabetically (save to m3u)
    5 - Merge all json files
    7 -
    """
    # Step 1
    m3u_list = get_m3u_from_url(url)

    # Step 2
    ext_inf = remove_duplicate_urls(m3u_list)

    # Step 3
    save_file_in_m3u(ext_inf, f"{url_name}.m3u")  # Changed variable_name to url


# Cargar el archivo JSON
with open('src/utils/URLS.json', 'r') as file:
    urls = json.load(file)
# Iterar sobre cada elemento del JSON y ejecutar get_all_m3u_from_url con el valor correspondiente
for url_name, url_value in urls.items():
    print(f"Ejecutando get_all_m3u_from_url para {url_name}: {url_value}")
    get_all_m3u_from_url(url_value)

# Step 4
merge_m3u_to_json()

# Step optional, delete NSFW content
topics_to_delete = ['xxx', 'adult']
remove_channels_from_json("ALL_CHANNELS.json", topics_to_delete)

# Step 5
list_key_names("ALL_CHANNELS.json")

# Step 6
json_to_m3u("ALL_CHANNELS.json")
