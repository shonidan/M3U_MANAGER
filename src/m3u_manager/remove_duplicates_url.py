def remove_duplicate_urls(url_list):
    if url_list is None:
        return []

    seen_urls = set()
    unique_urls = []

    for tup in url_list:
        url = tup[1]  # Get the second element of the tuple (the URL)
        if url not in seen_urls:
            unique_urls.append(tup)
            seen_urls.add(url)

    return unique_urls
