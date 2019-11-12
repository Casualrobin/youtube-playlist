from bs4 import BeautifulSoup
import requests
import re
import OutputManager

# url = "www.youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true"
# todo take cmd line arg(s)
# todo sanitise inputs better - https://youtube.com blah blah - accepted
# todo add tests


def sanitise_input(_url):
    _url = _url.strip('"')
    _url = _url.strip("'")
    if _url.__contains__("youtube.com"):
        # change protocol / domain to https://www.youtube.com
        proper_start = "https://www.youtube.com"
        if not _url.startswith(proper_start):
            start = r"(?i)^.*youtube.com"
            _url = re.sub(start, proper_start, _url)
    else:
        print()
    return _url


def validate_url(_url):
    if "youtube.com" in _url:
        return True
    else:
        return False


def validate_output_location(_output):
    if _output == "terminal" or _output == "txt" or _output == "csv":
        return True
    else:
        return False

print("Hello! This application will save the track list from a YouTube playlist.")
url = input("Please enter a YouTube playlist URL to download a track list from: ")

is_youtube = False

while not is_youtube:
    is_youtube = validate_url(url)
    if is_youtube:
        break
    else:
        url = input("This program can only scrape YouTube. Please enter a valid YouTube URL:")

url = sanitise_input(url)

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

is_valid_output = False
output_type = input("Enter an output type - terminal / txt / csv: ")
while not is_valid_output:
    is_valid_output = validate_output_location(output_type)
    if is_valid_output:
        break
    else:
        output_type = input("Please enter a valid output type - terminal / txt / csv: ")

OutputManager = OutputManager.OutputManager(output_type, soup)

if output_type == 'terminal':
    OutputManager.output_to_terminal()
elif output_type == 'txt':
    OutputManager.output_to_txt()
elif output_type == 'csv':
    OutputManager.output_to_csv()

