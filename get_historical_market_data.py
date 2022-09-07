import yfinance as yf
from draw import *
import pandas as pd
import matplotlib.pyplot as plt


class GetHistoricalData:
    def __init__(self, company_ticker, default_location):
        self.company_ticker = company_ticker
        self.default_location = default_location

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

    def get_historical_data(self):
        stock_data = self.get_stock_historical_data_5y()
        df = pd.DataFrame(stock_data)
        open_data = df["Open"]
        # data = stock_data.loc[:, "Open"].copy()
        plt.style.use("dark_background")
        open_data.plot(color="#77BC3F")
        plt.style.use("dark_background")
        plt.margins(0.1, 0.1)
        plt.title(f"{self.company_ticker} Stock Evolution", fontweight='bold', size=16)
        plt.ylabel("Price ($)", fontweight='bold')
        plt.savefig(f'{self.default_location}\exported_photos\{self.company_ticker}\{self.company_ticker}.png', bbox_inches='tight')
        plt.clf()
        image_to_be_updated = self.default_location + '\\default_image\\single_default.png'
        img = Image.open(image_to_be_updated)
        chart_image_open = Image.open(f'{self.default_location}\exported_photos\{self.company_ticker}\{self.company_ticker}.png')
        image_w, image_h = img.size
        stock_evolution = chart_image_open.resize((800, 700))
        net_w, net_h = stock_evolution.size
        offset = ((image_w - net_w) // 2, (image_h - net_h) // 2)
        img.paste(stock_evolution, offset, stock_evolution)
        img.save(f'{self.default_location}\exported_photos\{self.company_ticker}\{self.company_ticker}.png')

