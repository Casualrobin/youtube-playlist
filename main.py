from bs4 import BeautifulSoup
import requests
import re


#url = input("Enter a website to extract the URL's from: ")
#r  = requests.get("http://" +url)


r = requests.get("https://www.youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true")
data = r.text
soup = BeautifulSoup(data)

for td in soup.find_all('td'):
  # Class is held in a list.
  if td.get('class')[0] == 'pl-video-title':
    for var in td.find_all('a'):
      if var.get('class')[0] == 'pl-video-title-link':
        print('Song: ' + var.get_text().strip())
        print('Link: www.youtube.com'+ var.get('href'))
    for div in td.find_all('div'):
      if div.get('class')[0] == 'pl-video-owner':
        print('Artist / Video Channel: ' + div.get_text().strip())
    print('---------------------------------------')
