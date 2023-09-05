from typing import List
from inventory import InventoryManager
from reporting import ReportGenerator

if __name__ == "__main__":
    inventory_manager = InventoryManager()
    report_generator = ReportGenerator()

    initial_inventory = inventory_manager.inventory
    
    print(report_generator.generate_inventory_report(initial_inventory))
    
    item_to_purchase = "apple"
    quantity_to_purchase = 5
    if inventory_manager.is_item_available(item_to_purchase, quantity_to_purchase):
        if inventory_manager.purchase_item(item_to_purchase, quantity_to_purchase):
            print(f"{quantity_to_purchase} {item_to_purchase}(s) purchased.")
        else:
            print("Purchase failed due to insufficient stock.")
    
    purchases = [("banana", 10), ("orange", 15)]
    inventory_manager.process_multiple_purchases(purchases)
    
    print(report_generator.generate_inventory_report(initial_inventory))
