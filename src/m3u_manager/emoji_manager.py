import json
import re


def replace_emojis_from_file(filename):
    emoji_mapping = {
        "❌": "X",
        # Agrega más emojis y sus representaciones de texto aquí si es necesario
    }

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for group_key, channels in list(data.items()):
        new_group_key = ""
        for char in group_key:
            # Solo reemplazar emojis que están en emoji_mapping
            if char in emoji_mapping:
                new_group_key += emoji_mapping[char]
            else:
                new_group_key += char

        data[new_group_key] = data.pop(group_key)

        for channel in channels:
            if "info" in channel:
                new_info = ""
                for char in channel["info"]:
                    # Solo reemplazar emojis que están en emoji_mapping
                    if char in emoji_mapping:
                        new_info += emoji_mapping[char]
                    else:
                        new_info += char
                channel["info"] = new_info

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def remove_emojis_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # Procesar los datos para eliminar emojis
    for group_key in list(json_data.keys()):
        # Eliminar emojis del nombre del grupo
        new_group_key = remove_emojis(group_key)
        if new_group_key != group_key:
            json_data[new_group_key] = json_data.pop(group_key)

        # Eliminar emojis de la información de cada canal
        for item in json_data[new_group_key]:
            if isinstance(item['info'], str):
                item['info'] = remove_emojis(item['info'])

    # Escribir los datos procesados de vuelta al mismo archivo
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


def remove_emojis(text):
    # Patrón de regex para encontrar emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticones
                               u"\U0001F300-\U0001F5FF"  # símbolos y pictogramas
                               u"\U0001F680-\U0001F6FF"  # transporte y símbolos de mapa
                               u"\U0001F1E0-\U0001F1FF"  # banderas (iOS)
                               u"\U00002500-\U00002BEF"  # caracteres chinos comunes
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               u"\u2013"
                               u"\u2122"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)