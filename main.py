import os

from utils import check_and_create_folder
import get_financial
from get_basic_info import *
from get_historical_market_data import *
from create_metadata import *
from create_structure import *

default_location = os.getcwd()
exported_info_folder = default_location + "\exported_info"
# default_photo_folder = default_location + "\default_image"


def create_structure():
    create_folder_structure = CreateStructureFolder(default_location)
    create_folder_structure.create_structure()
    create_folder_structure.create_default_image()


def create_info_files(company):
    print(f"Extracting informations about the {company} in csv files...")
    create_metadata = CreateMetadata(company, default_location)
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


def create_main_image(company_ticker):
    os.chdir(default_location)
    print(f"Start getting the information for the {company_ticker} stock...")
    invest_class = Investing(company_ticker, exported_info_folder)
    stock_information = invest_class.get_stock_information()
    print(f"Creating photo for {company_ticker} ticker...")
    invest_class.draw_stock_information(stock_information)
    print(f"Updating photo with the {company_ticker} logo...")
    invest_class.update_photo_company_logo(stock_information["ticker"], stock_information["logo_url"])


def create_financial_charts(company):
    get_financials = get_financial.GetFinancials(company, exported_info_folder)
    print(f"Creating plot to see Financials details about {company}")
    company_folder = check_and_create_folder(f'\{company}')
    os.chdir(company_folder)
    get_financials.default_net_income(default_location, column_name="Net Income")
    get_financials.default_net_income(default_location, column_name="Research Development")
    get_financials.default_net_income(default_location, column_name="Income Before Tax")
    get_financials.default_net_income(default_location, column_name="Gross Profit")
    get_financials.default_net_income(default_location, column_name="Ebit")
    get_financials.default_net_income(default_location, column_name="Gross Profit")
    get_financials.default_net_income(default_location, column_name="Total Revenue")
    get_financials.default_net_income(default_location, column_name="Income Before Tax")


if __name__ == '__main__':
    company_list = ["AAPL", "MSFT", "TSLA", "AMZN"]

    print(f'Creating the structure folders...')
    create_structure()

    for company in company_list:
        create_info_files(company)
        create_main_image(company)
        create_financial_charts(company)
