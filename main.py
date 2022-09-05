import get_financial
from get_basic_info import *
from get_historical_market_data import *
from create_metadata import *

default_location = os.getcwd()
exported_info_folder = default_location + "\exported_info"
print(exported_info_folder)

if __name__ == '__main__':
    company_list = ["AAPL", "MSFT", "TSLA"]
    company = "MSFT"
    create_metadata = CreateMetadata(company, default_location)
    invest_class = Investing(company, exported_info_folder)
    create_metadata.create_basic_info_file()
    stock_information = invest_class.get_stock_information()
    invest_class.draw_stock_information(stock_information)
    # for company in company_list:
    #     invest_class = Investing(company, exported_info_folder)
    #     print(f"Start getting the information for the {company} stock...")
    #     stock_information = invest_class.get_stock_information()
    #     invest_class.draw_stock_information(stock_information)
    #     invest_class.update_photo_company_logo(stock_information["ticker"], stock_information["logo_url"])

    # get_financials = get_financial.GetFinancials("MSFT")
    # get_financials.create_net_income_plot()
