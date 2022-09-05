from PIL import Image, ImageDraw, ImageFont
from api import GetDomainLogo
import os
default_location = os.getcwd()

def check_and_create_folder(folder_name="\exported_photos"):
    print(f'The current working directory is: {default_location}')
    folder_location = default_location + folder_name
    print(f'Create folder were photos will be exported...')
    if os.path.isdir(folder_location):
        print(f'The {folder_name} already exists! Continuing...')
    else:
        os.mkdir(folder_location)
        print(f'{folder_name} created! Location: {folder_location}')
    return folder_location

def open_fonts(font_path,size):
    """ This function is used to initialize fonts """
    my_font = ImageFont.truetype(font_path, size)
    return my_font

def initialize_fonts(default_fonts_location=r"C:\Users\Chelariu's\PycharmProjects\BeforeInvesting\\fonts\\", font_name="AppleGaramond.ttf"):
    """ This function is used to initialize fonts location """
    return default_fonts_location + font_name

def draw_stock_information(ticker="AAPL", company_short_name="APPLE Inc", company_sector="Technology", company_industry="Consumer Electronics", market_cap="2.7T",
                           dividend_yield=''):
    font_location = initialize_fonts()
    main_font = open_fonts(font_location, 60)
    second_font = open_fonts(font_location, 50)
    folder_location = check_and_create_folder()
    img = Image.open(r"C:\Users\Chelariu's\PycharmProjects\BeforeInvesting\default_photos\\single_default.png")
    draw_image = ImageDraw.Draw(img)
    font_color = "#FFFFFF"
    draw_image.text((400, 150), company_short_name + "(" + ticker + ")", fill=font_color, font=main_font,
                    align="center")
    draw_image.text((200, 200), company_industry + " | " + company_sector, fill=font_color, font=second_font,
                    align="center")
    draw_image.text((50, 300), "Market Cap: " + str(market_cap), fill=font_color, font=second_font, align="left")
    if str(dividend_yield) != "":
        draw_image.text((50, 350), "Dividend yield: " + str(dividend_yield) + '%', fill=font_color, font=second_font, align="left")
    else:
        draw_image.text((50, 350), "Dividend yield: 0%", fill=font_color, font=second_font,
                        align="left")
    img.show(img)


draw_stock_information()