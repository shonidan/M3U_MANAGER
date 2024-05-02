import json


def fix_json(file_name):
    def process_data(data):
        for group_name, channels in data.items():
            for channel in channels:
                if 'group-title=\"\",' in channel['info']:
                    channel['info'] = channel['info'].replace('group-title=\"\",', f'group-title=\"{group_name}\",')
                elif 'group-title=\" ' in channel['info']:
                    channel['info'] = channel['info'].replace('group-title=\"', f'group-title=\"{group_name}\",')

    def fix_group_names(data):
        for group_name in list(data.keys()):
            if group_name.startswith("_"):
                new_group_name = group_name.replace("_", "", 1)
                data[new_group_name] = data.pop(group_name)

    # Leer el JSON desde el archivo
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Llamar a la función interna para arreglar los nombres de grupo
    fix_group_names(data)

    # Llamar a la función interna para procesar los datos
    process_data(data)

    # Escribir el JSON actualizado de nuevo al archivo
    with open('ALL_CHANNELS.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
