from numerize import numerize
from PIL import ImageFont
import os
from datetime import date


def calculate_dividend_yield(dividend_rate, current_price):
    return round(((dividend_rate / current_price) * 100), 3)


def calculate_long_numbers(long_number):
    return numerize.numerize(long_number)


def check_and_create_folder(folder_name="exported_photos"):
    default_location = os.getcwd()
    print(f'The current working directory is: {default_location}')
    folder_location = default_location + "\\" + folder_name
    # default_location +
    print(f'Create folder were info will be exported...')
    if os.path.isdir(folder_location):
        print(f'The {folder_name} already exists! Continuing...')
    else:
        os.mkdir(folder_location)
        print(f'{folder_name} created! Location: {folder_location}')
    return folder_location


def get_photo_location(ticker, folder_location):
    image_name = ticker + ".png"
    folder_location = folder_location + '\\'
    os.chdir(folder_location)
    return folder_location + image_name


def open_fonts(font_path, size):
    """ This function is used to initialize fonts """
    my_font = ImageFont.truetype(font_path, size)
    return my_font


def save_photo(ticker, folder_location, img):
    image_name = ticker + ".png"
    os.chdir(folder_location)
    print(f'Creating {image_name} photo with basic information...')
    img.save(f"{ticker}.png")
    return folder_location + image_name


def get_date():
    today = date.today()
    current_date = today.strftime("%b-%d-%Y")
    return current_date