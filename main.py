from OutputManager import OutputManager
from WebScraper import WebScraper
import Validator

# url = "www.youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true"
# todo take cmd line arg(s)
# todo sanitise inputs better - https://youtube.com blah blah - accepted
# todo add tests
# todo would be nice to persist application, multiple urls, multiple output types

print("Hello! This application will save the track list from a YouTube playlist.")
url = input("Please enter a YouTube playlist URL to download a track list from: ")

is_youtube = False

while not is_youtube:
    is_youtube = Validator.validate_url(url)
    if is_youtube:
        break
    else:
        url = input("This program can only scrape YouTube. Please enter a valid YouTube URL:")

output_type = input("Enter an output type - terminal / txt / csv: ")

WebScraper = WebScraper(url)

output = WebScraper.get_list_of_songs()

is_valid_output = False

while not is_valid_output:
    is_valid_output = Validator.validate_output_location(output_type)
    if is_valid_output:
        break
    else:
        output_type = input("Please enter a valid output type - terminal / txt / csv: ")

OutputManager = OutputManager(output_type)

if output_type == 'terminal':
    OutputManager.output_to_terminal(output)
elif output_type == 'txt':
    OutputManager.output_to_txt(output)
elif output_type == 'csv':
    OutputManager.output_to_csv(output)

