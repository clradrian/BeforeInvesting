import os
import pandas as pd
import matplotlib.pyplot as plt
from numerize import numerize
from utils import calculate_long_numbers
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from utils import get_photo_location, check_and_create_folder


class GetFinancials:
    def __init__(self, company_ticker, exported_info_folder):
        self.company_ticker = company_ticker
        self.exported_info_folder = exported_info_folder

    def get_net_income_df(self, column_name):
        df_financials = pd.read_csv(f"{self.exported_info_folder}\{self.company_ticker}\{self.company_ticker}_financials_info.csv", index_col=0)
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
        folder_location = check_and_create_folder(folder_name="\exported_photos")
        x_axis, y_axis = self.change_axis()
        int_list = []
        for value in y_axis:
            delete_last_ch = value[:-1]
            get_last_ch = value[-1]
            int_list.append(float(delete_last_ch))
        plt.style.use('dark_background')
        plt.bar(x_axis, int_list, color="#77BC3F",
                width=0.6, edgecolor='white')
        plt.margins(0.1, 0.1)
        # plt.xlabel("Date")
        os.chdir(folder_location)
        plt.ylabel(f"Net Income ({get_last_ch})", fontweight='bold')
        plt.title(f"{self.company_ticker} - Net Income", fontweight='bold', size=16)
        plt.savefig(f'{self.company_ticker}_Net_Income.png', bbox_inches='tight')

    def default_net_income(self, default_location):
        os.chdir(default_location)
        default_image_location = default_location + '\\default_image'
        self.create_net_income_plot()
        image_to_be_updated = default_image_location + "\\single_default.png"
        img = Image.open(image_to_be_updated)
        os.chdir(default_location)
        folder_location = check_and_create_folder(folder_name="\exported_photos")
        net_income_image = get_photo_location(self.company_ticker + "_Net_Income", folder_location)
        net_income_image_open = Image.open(net_income_image)
        image_w, image_h = img.size
        net_income = net_income_image_open.resize((800, 700))
        net_w, net_h = net_income.size
        offset = ((image_w - net_w) // 2, (image_h - net_h) // 2)
        img.paste(net_income, offset, net_income)
        img.save(f"{self.company_ticker}_Net_Income_Updated.png")
