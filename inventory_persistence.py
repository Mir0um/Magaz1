import json

def save_inventory_to_file(inventory, filename):
    with open(filename, 'w') as file:
        json.dump(inventory, file)

def load_inventory_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise InventoryFileNotFoundError("Inventory file not found.")

