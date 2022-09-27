from draw import *
from utils import calculate_dividend_yield
from utils import calculate_long_numbers
import os, json


class Investing(Draw):
    def __init__(self, company_ticker, exported_info_folder):
        self.company_ticker = company_ticker
        self.exported_info_folder = exported_info_folder

    def read_basic_info_file(self):
        for company_name in os.listdir(self.exported_info_folder):
            if company_name == self.company_ticker:
                with open(f"{self.exported_info_folder}/{self.company_ticker}/{self.company_ticker}_basic_info.json", 'r') as basic_info:
                    basic_info_data = json.load(basic_info)
        return basic_info_data


    def get_stock_information(self):
        """ This function return the activity sector for a company using yfinance library. """
        company_info = self.read_basic_info_file()
        dict_ticker = {}
        try:
            dict_ticker["ticker"] = self.company_ticker
            dict_ticker["company_sector"] = company_info['sector']
            dict_ticker["company_industry"] = company_info['industry']
            dict_ticker["company_short_name"] = company_info['shortName']
            dict_ticker["current_price"] = company_info['currentPrice']
            dict_ticker["total_revenue"] = company_info['totalRevenue']
            dict_ticker["trailing_PE"] = company_info['trailingPE']
            dict_ticker["forward_PE"] = company_info['forwardPE']
            dict_ticker["trailing_Eps"] = company_info['trailingEps']
            dict_ticker["forward_Eps"] = company_info['forwardEps']
            dict_ticker["target_low_price"] = company_info['targetLowPrice']
            dict_ticker["target_mean_price"] = company_info['targetMeanPrice']
            dict_ticker["target_high_price"] = company_info['targetHighPrice']
            dict_ticker["fifty_two_week_low"] = company_info['fiftyTwoWeekLow']
            dict_ticker["fifty_two_week_high"] = company_info['fiftyTwoWeekHigh']
            dict_ticker["day_low"] = company_info["dayLow"]
            dict_ticker["day_high"] = company_info["dayHigh"]
            dict_ticker["logo_url"] = company_info['logo_url']

        except Exception as e:
            print(e)
        dividend_yield = ''
        if company_info['dividendRate']:
            dividend_rate = company_info['dividendRate']
            dict_ticker["dividend_yield"] = calculate_dividend_yield(dividend_rate, dict_ticker["current_price"])
        market_cap = company_info['marketCap']
        dict_ticker["transformed_market_cap"] = calculate_long_numbers(market_cap)
        dict_ticker["transformed_revenue"] = calculate_long_numbers(dict_ticker["total_revenue"])
        dict_ticker["profit_Margins"] = company_info['profitMargins']
        print(dict_ticker)
        return dict_ticker