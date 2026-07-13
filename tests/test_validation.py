"""Smoke tests for validation."""
import unittest

from astronomy_optimizer import validation


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(validation, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(validation) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
