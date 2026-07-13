"""Smoke tests for config."""
import unittest

from astronomy_optimizer import config


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(config, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(config) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
