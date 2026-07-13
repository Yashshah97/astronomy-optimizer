import unittest
from unittest.mock import Mock
from astronomy_optimizer import cli

class TestCLI(unittest.TestCase):

    def test_create_parser(self):
        parser = cli.create_parser()
        self.assertIsInstance(parser, cli.ArgumentParser)

    def test_parse_args(self):
        args = cli.parse_args(['--strategy', 'random'])
        self.assertEqual(args['strategy'], 'random')

if __name__ == '__main__':
    unittest.main()
