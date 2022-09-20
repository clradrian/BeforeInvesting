import os
import pandas as pd
import matplotlib.pyplot as plt
from numerize import numerize
from utils import calculate_long_numbers
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from utils import get_photo_location, check_and_create_folder


class Informations:
    def __init__(self, company_ticker, exported_info_folder, get_info):
        self.company_ticker = company_ticker
        self.exported_info_folder = exported_info_folder
        self.get_info = get_info

    def get_cashflow_df(self, column_name):
        df_financials = pd.read_csv(
            f"{self.exported_info_folder}\{self.company_ticker}\{self.company_ticker}_{self.get_info}_info.csv",
            index_col=0)
        t_get_df_financials = df_financials.T
        get_net_income_column = t_get_df_financials[column_name]
        return get_net_income_column

    def change_axis(self, column_name, quarterly):
        df_balance_sheet_income = self.get_cashflow_df(column_name)
        date_axis = []
        for date in list(df_balance_sheet_income.index.values):
            new_date = pd.to_datetime(date)
            datetime_object = datetime.strptime(str(new_date.date()), "%Y-%m-%d").strftime('%b-%Y')
            date_axis.append(datetime_object)

        transformed_values = []
        for x in df_balance_sheet_income.head():
            new_values = calculate_long_numbers(x)
            transformed_values.append(new_values)
        if quarterly:
            return sorted(date_axis), sorted(transformed_values)
        else:
            return sorted(date_axis), sorted(transformed_values)

    def create_plot(self, column_name, quarterly):
        folder_location = check_and_create_folder(folder_name="\exported_photos")
        x_axis, y_axis = self.change_axis(column_name, quarterly)
        int_list = []
        for value in y_axis:
            delete_last_ch = value[:-1]
            get_last_ch = value[-1]
            int_list.append(float(delete_last_ch))
        plt.style.use('classic')
        plt.bar(x_axis, int_list, color="#000066",
                width=0.6)
                # , edgecolor='white')
        plt.margins(0.1, 0.1)
        # plt.xlabel("Date")
        os.chdir(folder_location)
        plt.ylabel(f"{column_name} ({get_last_ch})", fontweight='bold')
        plt.title(f"{self.company_ticker} - {column_name}", fontweight='bold', size=16)
        company_location = check_and_create_folder(folder_name=f"\{self.company_ticker}")
        os.chdir(company_location)
        plt.savefig(f'{self.company_ticker}_{column_name}.png', bbox_inches='tight')
        plt.clf()

    def default_sheet(self, default_location, column_name, quarterly=None):
        os.chdir(default_location)
        self.create_plot(column_name, quarterly)
        image_to_be_updated = default_location + '\\default_image\\single_default.png'
        img = Image.open(image_to_be_updated)
        os.chdir(default_location)
        # folder_location = check_and_create_folder(folder_name="\exported_photos")
        net_income_image = get_photo_location(self.company_ticker + "_" + column_name,
                                              default_location + f'\\exported_photos\\{self.company_ticker}')
        net_income_image_open = Image.open(net_income_image)
        image_w, image_h = img.size
        net_income = net_income_image_open.resize((800, 700))
        net_w, net_h = net_income.size
        offset = ((image_w - net_w) // 2, (image_h - net_h) // 2)
        img.paste(net_income, offset, net_income)
        # company_location = check_and_create_folder(folder_name=f"\{self.company_ticker}")
        # os.chdir(company_location)
        os.remove(net_income_image)
        img.save(f"{self.company_ticker}_{self.get_info}_{column_name}.png")
