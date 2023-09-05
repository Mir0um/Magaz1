import unittest
from reporting import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.report_generator = ReportGenerator()

    def test_generate_inventory_report(self):
        inventory = {"apple": 50, "banana": 25, "orange": 33}
        report = self.report_generator.generate_inventory_report(inventory)
        self.assertIn("apple", report)
        self.assertIn("banana", report)
        self.assertIn("orange", report)

if __name__ == '__main__':
    unittest.main()
