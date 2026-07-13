"""Smoke tests for io_utils."""
import unittest

from astronomy_optimizer import io_utils


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(io_utils, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(io_utils) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
