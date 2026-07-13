import unittest
from unittest.mock import patch, MagicMock
from astronomy_optimizer import io_utils

class TestIoUtils(unittest.TestCase):

    def test_read_csv(self):
        with patch('builtins.open', return_value=MagicMock(spec=file)) as mock_open:
            mock_reader = MagicMock()
            mock_reader.__iter__.return_value = [{'key': 'value'}]
            mock_open.return_value.__enter__.return_value.reader = mock_reader
            self.assertEqual(io_utils.read_csv('test.csv'), [{'key': 'value'}])

    def test_write_csv(self):
        with patch('builtins.open', return_value=MagicMock(spec=file)) as mock_open:
            mock_writer = MagicMock()
            io_utils.write_csv('test.csv', [{'key': 'value'}])
            mock_open.assert_called_once_with('test.csv', 'w', newline='')
            mock_writer.writeheader.assert_called_once()
            mock_writer.writerows.assert_called_once_with([{'key': 'value'}])

    def test_read_text(self):
        with patch('builtins.open', return_value=MagicMock(spec=file)) as mock_open:
            mock_f = MagicMock()
            mock_f.readlines.return_value = ['line1\n', 'line2\n']
            mock_open.return_value.__enter__.return_value = mock_f
            self.assertEqual(io_utils.read_text('test.txt'), ['line1', 'line2'])

    def test_write_text(self):
        with patch('builtins.open', return_value=MagicMock(spec=file)) as mock_open:
            io_utils.write_text('test.txt', ['line1', 'line2'])
            mock_open.assert_called_once_with('test.txt', 'w')
            mock_f = mock_open.return_value.__enter__.return_value
            self.assertEqual(mock_f.write.call_args_list, [
                call('line1\n'),
                call('line2\n')
            ])

if __name__ == '__main__':
    unittest.main()
