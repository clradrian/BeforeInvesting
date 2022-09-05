import os

import yfinance as yf
import json
from utils import check_and_create_folder

class CreateMetadata:
    def __init__(self, company_ticker, default_location):
        self.company_ticker = company_ticker
        self.default_location = default_location

    def get_all_info(self):
        stock_ticker = yf.Ticker(self.company_ticker)
        return stock_ticker

    def create_basic_info_file(self):
        basic_info = self.get_all_info().info
        os.chdir(self.default_location)
        print(f'{os.chdir(self.default_location)}', "----------")
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        with open(f"{self.company_ticker}_basic_info.json", "w") as outfile:
            json.dump(basic_info, outfile)
