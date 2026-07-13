"""Smoke tests for formatting."""
import unittest

from astronomy_optimizer import formatting


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(formatting, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(formatting) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
