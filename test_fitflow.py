import unittest
from fitflow_logic import calculate_total_weight

class TestFitFlowStats(unittest.TestCase):
    def test_calculate_total_weight(self):
        workout = [(100, 10), (100, 10), (100, 10)]
        self.assertEqual(calculate_total_weight(workout), 3000)

    def test_empty_workout(self):
        self.assertEqual(calculate_total_weight([]), 0)

if __name__ == '__main__':
    unittest.main()