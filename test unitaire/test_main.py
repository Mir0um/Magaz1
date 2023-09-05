import unittest
from unittest.mock import patch
from main import inventory_manager, report_generator

class TestMainFunctionality(unittest.TestCase):
    @patch("builtins.input", side_effect=["apple", "5"])
    def test_main_purchase_item(self, mock_input):
        initial_quantity = inventory_manager.inventory["apple"]
        inventory_manager.purchase_item = lambda *_: True
        inventory_manager.is_item_available = lambda *_: True
        inventory_manager.process_multiple_purchases = lambda *_: None
        initial_report = report_generator.generate_inventory_report(inventory_manager.inventory)
        
        with patch("builtins.print") as mock_print:
            exec(open("main.py").read())
            mock_print.assert_any_call("5 apple(s) purchased.")
        
        updated_quantity = inventory_manager.inventory["apple"]
        self.assertEqual(updated_quantity, initial_quantity - 5)
        
        updated_report = report_generator.generate_inventory_report(inventory_manager.inventory)
        self.assertNotEqual(initial_report, updated_report)

if __name__ == '__main__':
    unittest.main()
