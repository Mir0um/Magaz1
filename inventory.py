import json
from typing import Dict
from inventory_persistence import save_inventory_to_file, load_inventory_from_file

class InventoryManager:
    def __init__(self):
        self.inventory: Dict[str, int] = self.load_inventory_from_file("inventory.json")

    def save_inventory(self):
        save_inventory_to_file(self.inventory, "inventory.json")

    def load_inventory_from_file(self, filename):
        return load_inventory_from_file(filename)
    

    def is_item_available(self, item_id: str, quantity: int) -> bool:
        return item_id in self.inventory.keys() and self.inventory[item_id] >= quantity

    def purchase_item(self, item_id: str, quantity: int) -> bool:
        if item_id in self.inventory and self.inventory[item_id] >= quantity:
            self.inventory[item_id] -= quantity
            self.save_inventory_to_file("inventory.json")
            return True
        return False

    def process_multiple_purchases(self, purchase_list: list) -> None:
        for item_id, quantity in purchase_list:
            if item_id in self.inventory.keys() and self.inventory[item_id] >= quantity:
                self.inventory[item_id] -= quantity
                self.save_inventory_to_file("inventory.json")
