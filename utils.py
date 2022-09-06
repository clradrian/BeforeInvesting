from numerize import numerize
import os


def calculate_dividend_yield(dividend_rate, current_price):
    return round(((dividend_rate / current_price) * 100), 3)


def calculate_long_numbers(long_number):
    return numerize.numerize(long_number)


def check_and_create_folder(folder_name="\exported_photos"):
    default_location = os.getcwd()
    print(f'The current working directory is: {default_location}')
    folder_location = default_location + folder_name
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
