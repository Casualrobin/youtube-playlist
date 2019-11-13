import unittest
from unittest import mock
from src.OutputManager import OutputManager, create_output_directory


class OutputManager(unittest.TestCase):

    # todo add tests

    def setUp(self):
        pass

    def test_insert_delimiters(self):
        pass

    def test_add_titles_inline(self):
        pass

    def test_output_to_terminal(self):
        pass

    def test_output_to_txt(self):
        pass

    def test_output_to_csv(self):
        pass

    def test_create_output_directory(self, ):
        pass

    @mock.patch('src.OutputManager.os')
    def test_create_output_directory(self, mock_os):
        mock_os.rmdir('Output')
        create_output_directory()
        mock_os.mkdir.assert_called_with('Output')
