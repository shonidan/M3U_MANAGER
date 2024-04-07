import requests
import logging

def get_m3u_from_url(url):
    try:
        # New code added
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logging.info("URL Available")
            else:
                logging.info(f"{url} is not reachable (Status Code: {response.status_code}).")
                with open("error_urls.txt", "a") as f:
                    f.write(f"{url} (Status Code: {response.status_code})\n")
        except requests.ConnectionError:
            print(f"{url} is not reachable.")
            with open("error_urls.txt", "a") as f:
                f.write(f"{url} (Connection Error)\n")
        # End of new code

        response = requests.get(url)
        response.raise_for_status()  # Checks for errors in the response

        # If the response is successful, reads the content of the response
        content = response.text.splitlines()

        # List to store channel names and m3u/m3u8 links
        channel_names_and_url = []

        # Iterates over each line and looks for .m3u and .m3u8 links
        for i, line in enumerate(content):
            if line.strip().startswith(('https://', 'http://')) or line.strip().endswith(('.m3u', '.m3u8')):
                # Gets the channel name (previous line) if exists
                if i > 0:
                    channel_info = content[i - 1]
                else:
                    channel_info = None

                # Adds channel name and link to the list
                channel_names_and_url.append((channel_info, line.strip()))

        return channel_names_and_url

    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return []