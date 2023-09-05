#(contenant les fonctions liées à la gestion de l'inventaire) :
from typing import Dict

class InventoryManager:
    def __init__(self):
        self.inventory: Dict[str, int] = {"apple": 50, "banana": 25, "orange": 33}

    def is_item_available(self, item_id: str, quantity: int) -> bool:
        return item_id in self.inventory.keys() and self.inventory[item_id] >= quantity

    def purchase_item(self, item_id: str, quantity: int) -> bool:
        if item_id in self.inventory and self.inventory[item_id] >= quantity:
            self.inventory[item_id] -= quantity
            return True
        return False

    def process_multiple_purchases(self, purchase_list: list) -> None:
        for item_id, quantity in purchase_list:
            if item_id in self.inventory.keys() and self.inventory[item_id] >= quantity:
                self.inventory[item_id] -= quantity
