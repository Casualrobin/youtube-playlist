import unittest
from unittest import mock
from src.OutputManager import OutputManager, create_output_directory
import io


class TestOutputManager(unittest.TestCase):

    def setUp(self):
        pass

    def test_insert_delimiters(self):
        om = OutputManager('terminal')
        result = OutputManager.insert_delimiters(om, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        delim = '---------------------------------------'
        expected = ['a', 'b', 'c', delim, 'd', 'e', 'f', delim, 'g', 'h', 'i']
        self.assertEqual(result, expected)

    def test_add_titles_inline(self):
        om = OutputManager('terminal')
        result = OutputManager.add_titles_inline(om, ['a', 'b', 'c', 'd', 'e', 'f'])
        expected = ['Song: ' + 'a', 'Link: ' + 'b', 'Artist / Video Channel: ' + 'c',
                    'Song: ' + 'd', 'Link: ' + 'e', 'Artist / Video Channel: ' + 'f']
        self.assertEqual(result, expected)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_output_to_terminal(self, mock_stdout):
        om = OutputManager('terminal')
        OutputManager.output_to_terminal(om, ['a', 'b', 'c'])
        self.assertEqual(mock_stdout.getvalue(), 'Song: a\nLink: b\nArtist / Video Channel: c\n')

    def test_output_to_txt(self):
        with mock.patch('src.OutputManager.open', mock.mock_open()) as mocked_file:

            om = OutputManager('txt')
            om.output_to_txt(['a', 'b', 'c'])

            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with('Output/MySongs.txt', 'w+')

            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file
            calls = [mock.call().write('Song: a\n'), mock.call().write('Link: b\n'),
                     mock.call().write('Artist / Video Channel: c\n')]
            mocked_file.assert_has_calls(calls)

    def test_output_to_csv(self):
        with mock.patch('src.OutputManager.open', mock.mock_open()) as mocked_file:

            om = OutputManager('csv')
            om.output_to_csv(['a', 'b', 'c'])

            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with('Output/MySongs.csv', 'w+')

            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file

            calls = [mock.call('Output/MySongs.csv', 'w+'),
                     mock.call().__enter__(),
                     mock.call().write('Song,Link,Artist\r\n'),
                     mock.call().write('a,b,c\r\n'),
                     mock.call().__exit__(None, None, None)]
            mocked_file.assert_has_calls(calls)

    @unittest.skip("todo cannot mock checking if a file exists on the os")
    @mock.patch('src.OutputManager.os')
    def test_create_output_directory(self, mock_os):
        mock_os.rmdir('Output')
        create_output_directory()
        mock_os.mkdir.assert_called_with('Output')













