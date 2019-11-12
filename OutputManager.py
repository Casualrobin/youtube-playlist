import os
import re
import csv


class OutputManager:

    # todo we should not need a soup reference
    output_type = ""
    soup = ""

    def __init__(self, output_type, soup):
        self.output_type = output_type
        self.soup = soup

    def output_to_terminal(self):
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

    def output_to_txt(self):
        self.create_output_directory()
        f = open("Output/MySongs.txt", "w+")
        for td in self.soup.find_all('td'):
            # Class is held in a list.
            if td.get('class')[0] == 'pl-video-title':
                for var in td.find_all('a'):
                    if var.get('class')[0] == 'pl-video-title-link':
                        f.write('Song: ' + var.get_text().strip() + '\n')
                        f.write('Link: www.youtube.com' + var.get('href') + '\n')
                for div in td.find_all('div'):
                    if div.get('class')[0] == 'pl-video-owner':
                        if re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()):
                            f.write('Artist / Video Channel: ' + re.search(r'(?<=by ).+(?= - Topic)',
                                                                           div.get_text().strip()).group() + '\n')
                        elif re.search(r'(?<=by ).+', div.get_text().strip()):
                            f.write('Artist / Video Channel: ' + re.search(r'(?<=by ).+',
                                                                           div.get_text().strip()).group() + '\n')
                        else:
                            f.write('Regex did not match.' + '\n')
                        f.write('---------------------------------------' + '\n')
        f.close()

    def output_to_csv(self):
        self.create_output_directory()
        with open('Output/MySongs.csv', 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Song', 'Link', 'Artist'])
            for td in self.soup.find_all('td'):
                # Class is held in a list.
                if td.get('class')[0] == 'pl-video-title':
                    for var in td.find_all('a'):
                        if var.get('class')[0] == 'pl-video-title-link':
                            d1 = var.get_text().strip()
                            d2 = 'youtube.com' + var.get('href')
                    for div in td.find_all('div'):
                        if div.get('class')[0] == 'pl-video-owner':
                            if re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()):
                                d3 = re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()).group()
                            elif re.search(r'(?<=by ).+', div.get_text().strip()):
                                d3 = re.search(r'(?<=by ).+', div.get_text().strip()).group()
                            else:
                                d3 = 'Regex did not match.'
                    filewriter.writerow([d1, d2, d3])

    def create_output_directory(self):
            if not os.path.exists('Output'):
                os.mkdir('Output')
