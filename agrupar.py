import json

def read_urls_from_txt(txt_file):
    urls = []
    with open(txt_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("http"):
                urls.append(line)
    return urls

def save_urls_to_json(urls, json_file):
    data = {}
    for i, url in enumerate(urls, start=1):
        data[f"new_group_{i:02d}"] = url
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    txt_file = "urls.txt"  # Nombre de tu archivo de texto con las URLs
    json_file = "urls.json"  # Nombre del archivo JSON de salida

    urls = read_urls_from_txt(txt_file)
    save_urls_to_json(urls, json_file)
    print(f"Se han guardado las URLs en {json_file}")

if __name__ == "__main__":
    main()
