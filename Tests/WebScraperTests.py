import unittest
from src.WebScraper import WebScraper


class TestWebScraper(unittest.TestCase):

    def setUp(self):
        pass

    def test_sanitise_simple_input(self):
        w = WebScraper('https://www.youtube.com')
        self.assertEqual(WebScraper.sanitise_input(w, 'https://www.youtube.com'), "https://www.youtube.com")

    def test_sanitise_sanitary_input(self):
        w = WebScraper('https://www.youtube.com')
        self.assertEqual(WebScraper.sanitise_input(
            w, 'https://www.youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true'),
            'https://www.youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true')

    def test_sanitise_unsanitary_input(self):
        w = WebScraper('https://www.youtube.com')
        self.assertEqual(WebScraper.sanitise_input(
            w, '"youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true"'),
            'https://www.youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true')

    # todo
    def test_get_list_of_songs(self):
        pass
if __name__ == '__main__':
    unittest.main()