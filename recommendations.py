import pandas as pd

class Recommendations:
    def __init__(self, company_ticker, exported_info_folder):
        self.company_ticker = company_ticker
        self.exported_info_folder = exported_info_folder

    def get_recommendations_df(self):
        df_financials = pd.read_csv(
            f"{self.exported_info_folder}\{self.company_ticker}\{self.company_ticker}_recommendations_info.csv", index_col=0)
        list_of_evaluators = ["Barclays", "Citigroup", "Wells Fargo", "Morgan Stanley", "Deutsche Bank", "JP Morgan"]
        last_rows_df = df_financials.tail(20)
        only_big_banks = last_rows_df.loc[last_rows_df['Firm'].isin(list_of_evaluators)]
        print(only_big_banks)