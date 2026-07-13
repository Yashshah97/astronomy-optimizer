import unittest
from astronomy_optimizer import formatting

class TestFormatting(unittest.TestCase):

    def test_format_result(self):
        result = {'param1': 'value1', 'param2': 'value2'}
        self.assertEqual(formatting.format_result(result), "Optimization Result:\nparam1: value1\nparam2: value2\n")

    def test_format_grid_result(self):
        result = {'param1': 'value1', 'param2': 'value2'}
        self.assertEqual(formatting.format_grid_result(result), "Grid Search Result:\nparam1: value1\nparam2: value2\n")

    def test_format_annealing_result(self):
        result = {'param1': 'value1', 'param2': 'value2'}
        self.assertEqual(formatting.format_annealing_result(result), "Simulated Annealing Search Result:\nparam1: value1\nparam2: value2\n")

if __name__ == '__main__':
    unittest.main()
