import json

def list_key_names(json_file):
    try:
        with open(json_file, 'r', encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, dict):  # Check if the content is a dictionary
                idx_to_key = {}
                idx = 0
                for key, value in data.items():  # Iterate over the keys and values of the dictionary
                    idx += 1
                    idx_to_key[idx] = key
                    print(f"{idx}. {key}")

                total_dictionary_count = idx
                print(f"\nTotal dictionaries: {total_dictionary_count}")
                if total_dictionary_count > 0:
                    numbers_to_delete = input("Enter the numbers of the dictionaries you want to delete (separated by spaces): ")
                    numbers_to_delete = [int(num) for num in numbers_to_delete.split() if num.isdigit()]
                    if numbers_to_delete:
                        for number_to_delete in numbers_to_delete:
                            if 1 <= number_to_delete <= total_dictionary_count:
                                key_to_delete = idx_to_key[number_to_delete]
                                if key_to_delete in data:  # Check if the key is present in the dictionary
                                    del data[key_to_delete]  # Delete the dictionary entry
                                    print(f"The dictionary '{key_to_delete}' has been successfully deleted.")
                                else:
                                    print(f"The dictionary '{key_to_delete}' was not found.")
                            else:
                                print(f"Invalid dictionary number: {number_to_delete}")
                        with open(json_file, 'w') as f:
                            json.dump(data, f, indent=4)
                    else:
                        print("No dictionaries selected for deletion.")
                else:
                    print("No dictionaries to delete.")
            else:
                print("The JSON file does not contain a dictionary.")

    except FileNotFoundError:
        print(f"The file {json_file} does not exist.")
    except json.JSONDecodeError:
        print(f"The file {json_file} is not a valid JSON file.")

