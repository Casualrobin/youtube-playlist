import re


class WebScraper:

    soup = ""

    def __init__(self, soup):
        self.soup = soup

    def get_list_of_songs(self):
        for td in self.soup.find_all('td'):
            # Class is held in a list.
            if td.get('class')[0] == 'pl-video-title':
                for var in td.find_all('a'):
                    if var.get('class')[0] == 'pl-video-title-link':
                        print('Song: ' + var.get_text().strip())
                        print('Link: www.youtube.com' + var.get('href'))
                for div in td.find_all('div'):
                    if div.get('class')[0] == 'pl-video-owner':
                        if re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()):
                            print('Artist / Video Channel: ' + re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()).group())
                        elif re.search(r'(?<=by ).+', div.get_text().strip()):
                            print('Artist / Video Channel: ' + re.search(r'(?<=by ).+', div.get_text().strip()).group())
                        else:
                            print('Regex did not match.')
                        print('---------------------------------------')
