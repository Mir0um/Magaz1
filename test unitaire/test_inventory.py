import unittest
from inventory import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = InventoryManager()

    def test_is_item_available(self):
        self.assertTrue(self.inventory_manager.is_item_available("apple", 10))
        self.assertFalse(self.inventory_manager.is_item_available("banana", 30))

    def test_purchase_item(self):
        self.assertTrue(self.inventory_manager.purchase_item("apple", 10))
        self.assertFalse(self.inventory_manager.purchase_item("banana", 30))

    def test_process_multiple_purchases(self):
        purchase_list = [("apple", 5), ("banana", 10)]
        self.inventory_manager.process_multiple_purchases(purchase_list)
        self.assertEqual(self.inventory_manager.inventory["apple"], 35)
        self.assertEqual(self.inventory_manager.inventory["banana"], 15)

if __name__ == '__main__':
    unittest.main()