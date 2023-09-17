import unittest


class SumTestCase(unittest.TestCase):
    def test_sum_2_decimals(self):
        # Test 1: summary of 2 decimal values
        """
        Test that sum() will return summary of 2 decimal values
        """
        self.assertEqual(sum([3, 7]), 10)

    def test_sum_3_decimals(self):
        # Test 2: summary of 3 decimal values
        """
        Test that sum() will return summary of 3 decimal values
        """
        self.assertEqual(sum([2, 3, 7]), 12)


if __name__ == '__main__':
    unittest.main()
