import unittest
from optimal_change import my_optimal_change


class AssesmentTestCase(unittest.TestCase):
    """Tests for optimal_change.py"""

    def test_view_inventory(self):
        output_1 = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        self.assertEqual(my_optimal_change(62.13, 100), output_1)

    def test_second_case(self):
        '''Check for plural and commas'''
        output_2 = "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
        self.assertEqual(my_optimal_change(31.51, 50), output_2)


if __name__ == '__main__':
    unittest.main()