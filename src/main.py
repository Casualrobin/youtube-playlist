import Validator
import keyboard
from OutputManager import OutputManager
from WebScraper import WebScraper

# url = "www.youtube.com/playlist?list=PLvdtkdCcH2D3BWrdv2yMwIJ7-ScsklImS&disable_polymer=true"

print("Hello! This application will save the track list from a YouTube playlist. Ctrl-C to exit.")

while not keyboard.is_pressed('ctrl+c'):

    url = input("Please enter a YouTube playlist URL to download a track list from: ")

    is_youtube = False

    while not is_youtube:
        is_youtube = Validator.validate_url(url)
        if is_youtube:
            break
        else:
            url = input("This program can only scrape YouTube. Please enter a valid YouTube URL:")

    output_type = input("Enter an output type - terminal / txt / csv: ")

    web_scraper = WebScraper(url)

    output = web_scraper.get_list_of_songs()

    is_valid_output = False

    while not is_valid_output:
        is_valid_output = Validator.validate_output_location(output_type)
        if is_valid_output:
            break
        else:
            output_type = input("Please enter a valid output type - terminal / txt / csv: ")

    output_manager = OutputManager(output_type)
    output_manager.output_type = output_type

    if output_type == 'terminal':
        output_manager.output_to_terminal(output)
    elif output_type == 'txt':
        output_manager.output_to_txt(output)
    elif output_type == 'csv':
        output_manager.output_to_csv(output)



