from bs4 import BeautifulSoup
import re
import requests


class WebScraper:

    def __init__(self, url):
        url = self.sanitise_input(url)
        r = requests.get(url)
        data = r.text
        self.soup = BeautifulSoup(data)

    def sanitise_input(self, _url):
        _url = _url.strip('"')
        _url = _url.strip("'")
        if _url.__contains__("youtube.com"):
            proper_start = "https://www.youtube.com"
            if not _url.startswith(proper_start):
                start = r"(?i)^.*youtube.com"
                _url = re.sub(start, proper_start, _url)
        else:
            print()
        return _url

    def get_list_of_songs(self):
        ret = []
        for td in self.soup.find_all('td'):
            # Class is held in a list.
            if td.get('class')[0] == 'pl-video-title':
                for var in td.find_all('a'):
                    if var.get('class')[0] == 'pl-video-title-link':
                        ret.append('Song: ' + var.get_text().strip() + '\n')
                        ret.append('Link: www.youtube.com' + var.get('href') + '\n')
                for div in td.find_all('div'):
                    if div.get('class')[0] == 'pl-video-owner':
                        if re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()):
                            ret.append('Artist / Video Channel: ' + re.search(r'(?<=by ).+(?= - Topic)',
                                                                              div.get_text().strip()).group() + '\n')
                        elif re.search(r'(?<=by ).+', div.get_text().strip()):
                            ret.append('Artist / Video Channel: ' + re.search(r'(?<=by ).+',
                                                                              div.get_text().strip()).group() + '\n')
                        else:
                            ret.append('Regex did not match.' + '\n')
                        #ret.append('---------------------------------------' + '\n')

        return ret
