import unittest
from astronomy_optimizer import config

class TestConfig(unittest.TestCase):

    def test_default_config(self):
        self.assertEqual(config.config.search_strategy, 'grid')
        self.assertEqual(config.config.num_iterations, 1000)
        self.assertEqual(config.config.population_size, 50)
        self.assertEqual(config.config.temperature, 1.0)
        self.assertEqual(config.config.cooling_rate, 0.9)
        self.assertEqual(config.config.mutation_rate, 0.01)

    def test_load_config(self):
        config.load_config()
        self.assertIn('search_strategy', config.config)
        self.assertIn('num_iterations', config.config)
        self.assertIn('population_size', config.config)
        self.assertIn('temperature', config.config)
        self.assertIn('cooling_rate', config.config)
        self.assertIn('mutation_rate', config.config)

    def test_get_config(self):
        self.assertEqual(config.get('search_strategy'), 'grid')
        self.assertEqual(config.get('num_iterations'), 1000)
        self.assertIsNone(config.get('non_existent_key'))

if __name__ == '__main__':
    unittest.main()
