import yfinance as yf
from draw import *
import pandas as pd


class GetHistoricalData:
    def __init__(self, company_ticker):
        self.company_ticker = company_ticker

    def get_data_for_ticker(self):
        stock_ticker = yf.Ticker(self.company_ticker)
        return stock_ticker

    def get_stock_historical_data_max(self):
        """ This function return the activity sector for a company using yfinance library. """
        data_stock = self.get_data_for_ticker()
        hist = data_stock.history(period="max")
        return hist

    def get_stock_historical_data_5y(self):
        """ This function return the activity sector for a company using yfinance library. """
        data_stock = self.get_data_for_ticker()
        hist = data_stock.history(period="5y")
        return hist

    def get_historical_data_frame(self):
        five_y_historical = self.get_stock_historical_data_5y()
        pd.set_option('display.max_columns', None)
        df = pd.DataFrame(five_y_historical)