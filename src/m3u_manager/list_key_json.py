import json

def list_key_names(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

            if isinstance(data, dict):  # Verificar si el contenido es un diccionario
                idx_to_key = {}
                idx = 0
                for key, value in data.items():  # Iterar sobre las claves y valores del diccionario
                    idx += 1
                    idx_to_key[idx] = key
                    print(f"{idx}. {key}")

                total_dictionary_count = idx
                print(f"\nTotal de diccionarios: {total_dictionary_count}")
                if total_dictionary_count > 0:
                    numbers_to_delete = input("Ingrese los números de los diccionarios que desea eliminar (separados por espacios): ")
                    numbers_to_delete = [int(num) for num in numbers_to_delete.split() if num.isdigit()]
                    if numbers_to_delete:
                        for number_to_delete in numbers_to_delete:
                            if 1 <= number_to_delete <= total_dictionary_count:
                                key_to_delete = idx_to_key[number_to_delete]
                                if key_to_delete in data:  # Verificar si la clave está presente en el diccionario
                                    del data[key_to_delete]  # Eliminar la entrada del diccionario
                                    print(f"El diccionario '{key_to_delete}' ha sido eliminado exitosamente.")
                                else:
                                    print(f"No se encontró el diccionario '{key_to_delete}'.")
                            else:
                                print(f"Número de diccionario inválido: {number_to_delete}")
                        with open(json_file, 'w') as f:
                            json.dump(data, f, indent=4)
                    else:
                        print("No se han seleccionado diccionarios para eliminar.")
                else:
                    print("No hay diccionarios para eliminar.")
            else:
                print("El archivo JSON no contiene un diccionario.")

    except FileNotFoundError:
        print(f"El archivo {json_file} no existe.")
    except json.JSONDecodeError:
        print(f"El archivo {json_file} no es un archivo JSON válido.")
