import json
import re

def fix_json(file_name):
    def remove_special_characters_group_names(data):
        new_data = {}  # Nuevo diccionario con las claves modificadas
        for group_name, channels in data.items():
            # Eliminar caracteres especiales al principio del nombre del grupo
            new_group_name = re.sub(r'^[^a-zA-Z0-9]+', '', group_name)
            # Eliminar caracteres especiales al final del nombre del grupo
            new_group_name = re.sub(r'[^a-zA-Z0-9]+$', '', new_group_name)
            new_data[new_group_name] = channels

        return new_data

    def remove_intermediate_characters(data):
        new_data = {}  # Nuevo diccionario con las claves modificadas
        for group_name, channels in data.items():
            # Reemplazar caracteres intermedios no deseados entre palabras
            new_group_name = re.sub(r'[^a-zA-Z0-9/-_:]+', '_', group_name)
            new_data[new_group_name] = channels

        return new_data

    def remove_extra_underscores(data):
        new_data = {}  # Nuevo diccionario con las claves modificadas
        for group_name, channels in data.items():
            # Reemplazar múltiples guiones bajos con solo uno
            new_group_name = re.sub(r'_+', '_', group_name)
            new_data[new_group_name] = channels

        return new_data

    # Leer el JSON desde el archivo
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Modificar las claves del diccionario
    modified_data = remove_special_characters_group_names(data)

    # Aplicar la función para eliminar caracteres intermedios no deseados
    modified_data = remove_intermediate_characters(modified_data)

    # Aplicar la función para eliminar guiones bajos extras
    modified_data = remove_extra_underscores(modified_data)

    # Ordenar el diccionario por keys (group-title) alfabéticamente
    sorted_data = dict(sorted(modified_data.items()))

    # Escribir el JSON actualizado de nuevo al archivo
    with open('ALL_CHANNELS.json', 'w', encoding='utf-8') as file:
        json.dump(sorted_data, file, indent=4)
