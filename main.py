import get_financial
from get_basic_info import *
from get_historical_market_data import *
from create_metadata import *

default_location = os.getcwd()
exported_info_folder = default_location + "\exported_info"
print(exported_info_folder)

def create_info_files():
    create_metadata.create_basic_info_file()
    create_metadata.create_financials_info_file()
    create_metadata.create_quarterly_financials_info_file()
    create_metadata.create_balance_sheet_info_file()
    create_metadata.create_quarterly_balance_sheet_info_file()
    create_metadata.create_cashflow_info_file()
    create_metadata.create_quarterly_cashflow_info_file()
    create_metadata.create_earnings_info_file()
    create_metadata.create_quarterly_earnings_info_file()
    create_metadata.create_recommendations_info_file()


if __name__ == '__main__':
    company_list = ["AAPL", "MSFT", "TSLA"]
    for company in company_list:
        invest_class = Investing(company, exported_info_folder)
        create_metadata = CreateMetadata(company, default_location)
        get_financials = get_financial.GetFinancials(company, exported_info_folder)
        print(f"Extracting informations about the {company} in csv files...")
        create_info_files()
        print(f"Start getting the information for the {company} stock...")
        stock_information = invest_class.get_stock_information()
        print(f"Creating photo for {company} ticker...")
        invest_class.draw_stock_information(stock_information)
        print(f"Updating photo with the {company} logo...")
        invest_class.update_photo_company_logo(stock_information["ticker"], stock_information["logo_url"])
        print(f"Creating plot to see the Net Income for {company}")
        get_financials.create_net_income_plot()
