import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from numerize import numerize
# from matplotlib import style


class GetFinancials:
    def __init__(self, company_ticker):
        self.company_ticker = company_ticker

    def get_financial_data_for_ticker(self):
        stock_ticker = yf.Ticker(self.company_ticker)
        return stock_ticker.financials

    def calculate_long_numbers(self, long_number):
        return numerize.numerize(long_number)

    def get_net_income_df(self, column_name):
        get_df_financials = self.get_financial_data_for_ticker()
        t_get_df_financials = get_df_financials.T
        get_net_income_column = t_get_df_financials[[column_name]]
        return get_net_income_column

    def change_axis(self, column_name="Net Income"):
        df_net_income = self.get_net_income_df(column_name)
        date_axis = []
        for date in list(df_net_income.index.values):
            new_date = pd.to_datetime(date)
            # str(new_date.date())
            date_axis.append(str(new_date.date()))

        transformed_values = []
        for x in df_net_income[column_name].head():
            new_values = self.calculate_long_numbers(x)
            transformed_values.append(new_values)
        return sorted(date_axis), sorted(transformed_values)

    def create_net_income_plot(self):
        x_axis, y_axis = self.change_axis()
        int_list = []
        for value in y_axis:
            delete_last_ch = value[:-1]
            int_list.append(float(delete_last_ch))
        plt.style.use('dark_background')
        plt.bar(x_axis, int_list, color='green',
                width=0.5)
        plt.margins(0.3, 0.3)
        plt.xlabel("Date")
        plt.ylabel("Net Income")
        plt.title(f"{self.company_ticker} Net Income")
        plt.show()
