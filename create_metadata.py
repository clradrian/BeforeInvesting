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
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        with open(f"{self.company_ticker}_basic_info.json", "w") as outfile:
            json.dump(basic_info, outfile)


    def create_financials_info_file(self):
        financials_info = self.get_all_info().financials
        financials_info.columns = financials_info.columns.astype(str).str.replace(' ', '_')
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_financials_info.csv")

    def create_quarterly_financials_info_file(self):
        financials_info = self.get_all_info().quarterly_financials
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_quarterly_financials_info.csv")


    def create_balance_sheet_info_file(self):
        financials_info = self.get_all_info().balance_sheet
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_balance_sheet_info.csv")

    def create_quarterly_balance_sheet_info_file(self):
        financials_info = self.get_all_info().quarterly_balance_sheet
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_quarterly_balance_sheet_info.csv")

    def create_cashflow_info_file(self):
        financials_info = self.get_all_info().cashflow
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_cashflow_info.csv")

    def create_quarterly_cashflow_info_file(self):
        financials_info = self.get_all_info().quarterly_cashflow
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_quarterly_cashflow_info.csv")


    def create_earnings_info_file(self):
        financials_info = self.get_all_info().earnings
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_earnings_info.csv")

    def create_quarterly_earnings_info_file(self):
        financials_info = self.get_all_info().quarterly_earnings
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_quarterly_earnings_info.csv")

    def create_recommendations_info_file(self):
        financials_info = self.get_all_info().recommendations
        os.chdir(self.default_location)
        exported_info_location = check_and_create_folder("\exported_info")
        os.chdir(exported_info_location)
        company_ticker_folder = check_and_create_folder(f"\{self.company_ticker}")
        os.chdir(company_ticker_folder)
        financials_info.to_csv(f"{self.company_ticker}_recommendations_info.csv")
