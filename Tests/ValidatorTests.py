# unittest.main() provides a command-line interface to the test script.
# The above script is runnable from the command line,

import unittest
from src.Validator import *


class TestValidator(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate_urls(self):
        self.assertTrue(validate_url("youtube.com"))
        self.assertFalse(validate_url("youtube.net"))

    def test_validate_correct_output_locations(self):
        self.assertTrue(validate_output_location("terminal"))
        self.assertTrue(validate_output_location("txt"))
        self.assertTrue(validate_output_location("csv"))
        self.assertFalse(validate_output_location("xlsx"))

