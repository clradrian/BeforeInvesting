from PIL import Image, ImageDraw, ImageFont
from api import GetDomainLogo
import os
from datetime import date
from utils import get_photo_location, check_and_create_folder
from create_structure import *

class Draw:
    def __init__(self, image_path):
        self.image_path = image_path

    default_location = os.getcwd()

    def get_date(self):
        today = date.today()
        current_date = today.strftime("%b-%d-%Y")
        return current_date

    def open_fonts(self, font_path, size):
        """ This function is used to initialize fonts """
        my_font = ImageFont.truetype(font_path, size)
        return my_font


    def save_photo(self, ticker, folder_location, img):
        image_name = ticker + ".png"
        os.chdir(folder_location)
        print(f'Creating {image_name} photo with basic information...')
        img.save(f"{ticker}.png")
        return folder_location + image_name

    def draw_stock_information(self, stock_information):
        folder_location = check_and_create_folder()
        photo_location = self.default_location + '\\default_image\\single_default.png'
        img = Image.open(photo_location)
        draw_image = ImageDraw.Draw(img)
        font_location = self.default_location + '\\fonts\\AppleGaramond.ttf'
        main_font = self.open_fonts(font_location, 60)
        second_font = self.open_fonts(font_location, 40)
        info_font = self.open_fonts(font_location, 20)
        font_color = "#FFFFFF"
        header_font_color = "#ff0000"
        # self.center_text(img, main_font, stock_information["company_short_name"] + "(" + stock_information["ticker"] + ")",
        #                  stock_information["company_industry"] + " | " + stock_information["company_sector"], "Current Price: " + str(stock_information["current_price"]) + "$",
        #                  font_color)

        w, h = img.size  # get width and height of image
        t1_width, t1_height = draw_image.textsize(stock_information["company_short_name"] + "(" + stock_information["ticker"] + ")", main_font)  # Get text1 size
        t2_width, t2_height = draw_image.textsize(stock_information["company_industry"] + " | " + stock_information["company_sector"], second_font)  # Get text2 size
        t3_width, t3_height = draw_image.textsize("Current Price: " + str(stock_information["current_price"]) + "$", second_font)  # Get text3 size
        p1 = ((w - t1_width) / 2, h // 8.6)  # H-center align text1
        p2 = ((w - t2_width) / 2, h // 5.7)  # H-center align text2 + h // 5
        p3 = ((w - t3_width) / 2, h // 4.7)  # H-center align text3 + h // 2

        draw_image.text(p1, stock_information["company_short_name"] + "(" + stock_information["ticker"] + ")", fill=font_color, font=main_font,
                        align="center")
        draw_image.text(p2, stock_information["company_industry"] + " | " + stock_information["company_sector"], fill=font_color, font=second_font,
                        align="center")
        draw_image.text(p3, "Current Price: " + str(stock_information["current_price"]) + "$", fill=header_font_color, font=second_font, align="center")

        general_information_left_part = 50
        general_information_right_part = 320
        try:
            draw_image.text((general_information_left_part, general_information_right_part), "General Information:", fill=header_font_color, font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 40), "Market Cap: " + str(stock_information["transformed_market_cap"]), fill=font_color, font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 80), "Total Revenue: " + str(stock_information["transformed_revenue"]), fill=font_color, font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 120), "PE: " + str(stock_information["trailing_PE"]) + " | Forward PE: " + str(stock_information["forward_PE"]), fill=font_color, font=second_font,
                            align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 160), "EPS: " + str(stock_information["trailing_Eps"]) + " | Forward EPS: " + str(stock_information["forward_Eps"]), fill=font_color,
                            font=second_font, align="left")

            draw_image.text((general_information_left_part, general_information_right_part + 280), "Stock Price Targets: ", fill=header_font_color, font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 320), "LOW price: " + str(stock_information["target_low_price"]) + "$", fill=font_color, font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 360), "MEAN price: " + str(stock_information["target_mean_price"]) + "$", fill=font_color, font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 400), "HIGH price: " + str(stock_information["target_high_price"]) + "$", fill=font_color,
                            font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 460), "Stock Price Evolution: ",
                            fill=header_font_color, font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 500), "52 Week Range: " + str(stock_information["fifty_two_week_low"]) + "$ - " + str(stock_information["fifty_two_week_high"]) + "$",
                            fill=font_color, font=second_font, align="left")
            draw_image.text((general_information_left_part, general_information_right_part + 540), "Day's Range : " + str(stock_information["day_low"]) + "$ - " + str(stock_information["day_high"]) + "$",
                            fill=font_color, font=second_font, align="left")
            if "dividend_yield" in stock_information.keys():
                draw_image.text((general_information_left_part, general_information_right_part + 200), "Dividend yield: " + str(stock_information["dividend_yield"]) + '%', fill=font_color,
                                font=second_font, align="left")
            else:
                draw_image.text((general_information_left_part, general_information_right_part + 200), "Dividend yield: 0%", fill=font_color, font=second_font,
                                align="left")

            t4_width, t4_height = draw_image.textsize("*informations provided by Yahoo Finance", info_font)  # Get text3 size
            p4 = ((w - t4_width) / 2, h // 1.05)  # H-center align text1
            draw_image.text(p4, "*informations provided by Yahoo Finance", fill=font_color, font=info_font, align="center")

            current_date = self.get_date()
            t5_width, t5_height = draw_image.textsize("(" + current_date + ")", second_font)  # Get text3 size
            p5 = ((w - t5_width) / 2, h // 4.1)  # H-center align text1
            draw_image.text(p5, "(" + current_date + ")", fill=font_color, font=second_font)
        except:
            pass
        self.save_photo(stock_information["ticker"], folder_location, img)

    def update_photo_company_logo(self, ticker, url):
        os.chdir(self.default_location)
        folder_location = check_and_create_folder()
        image_to_be_updated = get_photo_location(ticker, folder_location)
        img = Image.open(image_to_be_updated).convert("RGBA")
        logo = GetDomainLogo(url).convert("RGBA")
        logo.putalpha(60) #blur photo
        img.paste(logo, (500, 500), logo)
        img.save(f"{ticker}.png")


