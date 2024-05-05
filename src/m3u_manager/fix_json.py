import json
import regex as re

def fix_json(file_name):
    def remove_special_characters_group_names(data):
        new_data = {}
        # Diccionario temporal para almacenar los canales agrupados por nombre de grupo
        temp_data = {}

        for group_name, channels in data.items():
            new_group_name = group_name
            # Eliminar caracteres especiales al principio del nombre del grupo
            new_group_name = re.sub(r'^[^\p{L}0-9]+', '', new_group_name)
            # Eliminar caracteres especiales al final del nombre del grupo
            new_group_name = re.sub(r'[^\p{L}0-9]+$', '', new_group_name)
            # Mantener solo los caracteres especiales permitidos en el medio del nombre del grupo
            new_group_name = re.sub(r'[^-\w:_\/]+', '_', new_group_name)

            # Verificar si el nuevo nombre ya existe en temp_data
            if new_group_name in temp_data:
                # Si el nuevo nombre existe, agregar los canales a la lista existente
                temp_data[new_group_name].extend(channels)
            else:
                # Si el nuevo nombre no existe, crear una nueva entrada en temp_data
                temp_data[new_group_name] = channels

        # Ahora, iterar sobre el diccionario temporal y consolidar los datos en new_data
        for group_name, channels in temp_data.items():
            # Verificar si el nombre del grupo ya existe en new_data
            if group_name in new_data:
                # Si el nombre del grupo existe, extender la lista de canales
                new_data[group_name].extend(channels)
            else:
                # Si el nombre del grupo no existe, crear una nueva entrada en new_data
                new_data[group_name] = channels

        return new_data

    def remove_extra_underscores(data):
        new_data = {}
        for group_name, channels in data.items():
            new_group_name = group_name
            # Reemplazar múltiples guiones bajos con solo uno
            new_group_name = re.sub(r'_+', '_', new_group_name)
            # Verificar si el nuevo nombre es diferente del original
            if new_group_name != group_name:
                # Si el nombre ha cambiado, agregar el canal al nuevo nombre
                if new_group_name not in new_data:
                    new_data[new_group_name] = []
                new_data[new_group_name].extend(channels)
            else:
                # Si el nombre no ha cambiado, mantener el nombre y los canales intactos
                new_data[group_name] = channels
        return new_data

    def update_group_title(data):
        for group_name, channels in data.items():
            for channel in channels:
                if 'info' in channel:
                    if 'group-title="' in channel['info']:
                        new_title = channel['info'].split('group-title="')[1].split('"')[0]
                        channel['info'] = channel['info'].replace('group-title="{}"'.format(new_title),
                                                                  'group-title="{}"'.format(group_name))

    def replace_specific_words(data, words_to_replace, replacement):
        new_data = {}
        for group_name, channels in data.items():
            new_group_name = group_name
            for word in words_to_replace:
                if word.lower() in group_name.lower():
                    new_group_name = replacement
                    break  # Salir del bucle una vez que se ha encontrado una coincidencia
            # Agregar el grupo original o el grupo modificado al nuevo diccionario
            if new_group_name not in new_data:
                new_data[new_group_name] = []
            new_data[new_group_name].extend(channels)
        return new_data

    # Leer el JSON desde el archivo
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Modificar las claves del diccionario
    modified_data = remove_special_characters_group_names(data)
    modified_data = remove_extra_underscores(modified_data)

    # Reemplazar palabras específicas en group_name
    words_to_replace = ['XXX', 'ADULT']
    replacement = 'ADULTS_XXX'
    modified_data = replace_specific_words(modified_data, words_to_replace, replacement)

    # Actualizar el valor de group-title en los datos
    update_group_title(modified_data)

    # Ordenar el diccionario por keys (group-title) alfabéticamente
    sorted_data = dict(sorted(modified_data.items()))

    # Escribir el JSON actualizado de nuevo al archivo
    with open('ALL_CHANNELS.json', 'w', encoding='utf-8') as file:
        json.dump(sorted_data, file, indent=4)
