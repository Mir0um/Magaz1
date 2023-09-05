#(contenant la fonction de génération de rapport) :

from typing import Dict

class ReportGenerator:
    def generate_inventory_report(self, inventory: Dict[str, int]) -> str:
        report = "Stock Report:\n"
        for item_id, quantity in inventory.items():
            report += f"Item ID: {item_id}, Quantity: {quantity}\n"
        return report
