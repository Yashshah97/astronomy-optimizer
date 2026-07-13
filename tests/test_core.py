import unittest
from astronomy_optimizer import core
import math


class TestCoreFunctions(unittest.TestCase):

    def test_grid_search(self):
        params = ['param1', 'param2']
        bounds = {'param1': (0, 10), 'param2': (0, 10)}
        best_params = core.grid_search(params, bounds)
        self.assertIsInstance(best_params, dict)

    def test_random_search(self):
        params = ['param1', 'param2']
        bounds = {'param1': (0, 10), 'param2': (0, 10)}
        num_samples = 100
        best_params = core.random_search(params, bounds, num_samples)
        self.assertIsInstance(best_params, dict)

    def test_simulated_annealing_search(self):
        params = ['param1', 'param2']
        bounds = {'param1': (0, 10), 'param2': (0, 10)}
        initial_temperature = 100
        best_params = core.simulated_annealing_search(params, bounds, initial_temperature)
        self.assertIsInstance(best_params, dict)


if __name__ == '__main__':
    unittest.main()
