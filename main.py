from bs4 import BeautifulSoup
import requests
import re
import os
import csv

# Get Data from Website.
url = input("Enter a website to extract the URL's from: ")
if not url:
  url = "www.youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true"
r = requests.get("https://" + url)
data = r.text
soup = BeautifulSoup(data)

output_type = input("Enter an output type - terminal / txt / csv: ")
if not output_type:
    output_type = 'terminal'

# If writing to file, configure output.
if output_type == 'txt' or output_type == 'csv':
  if not os.path.exists('Output'):
    os.mkdir('Output')
    if output_type == 'txt':
      f = open("Output/MySongs.txt", "w+")
    elif output_type == 'csv':
      with open('MySongs.csv', 'w+') as csvfile:
          filewriter = csv.writer(csvfile, delimiter=',',
                                  quotechar='|', quoting=csv.QUOTE_MINIMAL)
          filewriter.writerow(['Song', 'Link', 'Artist'])


if output_type == 'terminal':
  for td in soup.find_all('td'):
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

if output_type == 'txt':
  for td in soup.find_all('td'):
    # Class is held in a list.
    if td.get('class')[0] == 'pl-video-title':
      for var in td.find_all('a'):
        if var.get('class')[0] == 'pl-video-title-link':
          f.write('Song: ' + var.get_text().strip() + '\n')
          f.write('Link: www.youtube.com' + var.get('href') + '\n')
      for div in td.find_all('div'):
        if div.get('class')[0] == 'pl-video-owner':
          if re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()):
            f.write('Artist / Video Channel: ' + re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()).group() + '\n')
          elif re.search(r'(?<=by ).+', div.get_text().strip()):
            f.write('Artist / Video Channel: ' + re.search(r'(?<=by ).+', div.get_text().strip()).group() + '\n')
          else:
            f.write('Regex did not match.' + '\n')
          f.write('---------------------------------------' + '\n')
  f.close()

if output_type == 'csv':
  with open('MySongs.csv', 'w+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
      quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Song', 'Link', 'Artist'])
  for td in soup.find_all('td'):
    # Class is held in a list.
    if td.get('class')[0] == 'pl-video-title':
      for var in td.find_all('a'):
        if var.get('class')[0] == 'pl-video-title-link':
          d1 = 'Song: ' + var.get_text().strip()
          d2 = 'Link: www.youtube.com' + var.get('href')
      for div in td.find_all('div'):
        if div.get('class')[0] == 'pl-video-owner':
          if re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()):
            d3 = 'Artist / Video Channel: ' + re.search(r'(?<=by ).+(?= - Topic)', div.get_text().strip()).group()
          elif re.search(r'(?<=by ).+', div.get_text().strip()):
            d3 = 'Artist / Video Channel: ' + re.search(r'(?<=by ).+', div.get_text().strip()).group()
          else:
            d3 = 'Regex did not match.'
        filewriter.writerow(['d1', 'd2', 'd3'])
  csvfile.close()
