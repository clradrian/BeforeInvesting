import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from numerize import numerize
from utils import calculate_long_numbers
from datetime import datetime

class GetFinancials:
    def __init__(self, company_ticker):
        self.company_ticker = company_ticker

    def get_net_income_df(self, column_name):
        df_financials = pd.read_csv(r"C:\Users\Chelariu's\PycharmProjects\git\git_BeforeInvesting\BeforeInvesting\exported_info\MSFT\MSFT_financials_info.csv", index_col=0)
        t_get_df_financials = df_financials.T
        get_net_income_column = t_get_df_financials[column_name]
        return get_net_income_column

    def change_axis(self, column_name="Net Income"):
        df_net_income = self.get_net_income_df(column_name)
        date_axis = []
        for date in list(df_net_income.index.values):
            new_date = pd.to_datetime(date)
            datetime_object = datetime.strptime(str(new_date.date()), "%Y-%m-%d").strftime('%b-%Y')
            date_axis.append(datetime_object)

        transformed_values = []
        for x in df_net_income.head():
            new_values = calculate_long_numbers(x)
            transformed_values.append(new_values)
        return sorted(date_axis), sorted(transformed_values)

    def create_net_income_plot(self):
        x_axis, y_axis = self.change_axis()
        int_list = []
        for value in y_axis:
            delete_last_ch = value[:-1]
            get_last_ch = value[-1]
            int_list.append(float(delete_last_ch))
        plt.style.use('dark_background')
        plt.bar(x_axis, int_list, color='green',
                width=0.6)
        plt.margins(0.1, 0.1)
        # plt.xlabel("Date")
        plt.ylabel(f"Net Income ({get_last_ch})")
        plt.title(f"{self.company_ticker} Net Income")
        plt.show()
