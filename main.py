import os

from utils import check_and_create_folder
from get_basic_info import *
from create_metadata import *
from create_structure import *
import create_plots
import recommendations
import get_historical_market_data


default_location = os.getcwd()
exported_info_folder = default_location + "\exported_info"
exported_photos_folder = default_location + "\exported_photos"
# default_photo_folder = default_location + "\default_image"


def create_structure(company):
    create_folder_structure = CreateStructureFolder(default_location, company)
    create_folder_structure.create_structure()
    create_folder_structure.check_and_create_folder()
    # create_folder_structure.create_default_image()


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


def get_main_info(company):
    print(f"Extracting informations about the {company} in csv files...")
    create_metadata = CreateMetadata(company, default_location)
    create_metadata.create_basic_info_file()


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
    get_financials = create_plots.Informations(company, exported_info_folder, "financials")
    print(f"Creating plot to see Financials details about {company}")
    # company_folder = check_and_create_folder(f'\{company}')
    # os.chdir(company_folder)
    get_financials.default_sheet(default_location, column_name="Net Income")
    get_financials.default_sheet(default_location, column_name="Research Development")
    get_financials.default_sheet(default_location, column_name="Income Before Tax")
    get_financials.default_sheet(default_location, column_name="Gross Profit")
    get_financials.default_sheet(default_location, column_name="Ebit")
    get_financials.default_sheet(default_location, column_name="Gross Profit")
    get_financials.default_sheet(default_location, column_name="Total Revenue")
    get_financials.default_sheet(default_location, column_name="Income Before Tax")


def create_quarterly_financial_charts(company):
    get_financials = create_plots.Informations(company, exported_info_folder, "quarterly_financials")
    print(f"Creating plot to see Quarterly Financials details about {company}")
    # company_folder = check_and_create_folder(f'\{company}')
    # os.chdir(company_folder)
    get_financials.default_sheet(default_location, quarterly=True, column_name="Net Income")
    get_financials.default_sheet(default_location, quarterly=True, column_name="Research Development")
    get_financials.default_sheet(default_location, quarterly=True, column_name="Income Before Tax")
    get_financials.default_sheet(default_location, quarterly=True, column_name="Gross Profit")
    get_financials.default_sheet(default_location, quarterly=True, column_name="Ebit")
    get_financials.default_sheet(default_location, quarterly=True, column_name="Gross Profit")
    get_financials.default_sheet(default_location, quarterly=True, column_name="Total Revenue")
    get_financials.default_sheet(default_location, quarterly=True, column_name="Income Before Tax")


def create_balance_sheet_charts(company):
    get_balance_sheet = create_plots.Informations(company, exported_info_folder, "balance_sheet")
    print(f"Creating plot to see Balance Sheet details about {company}")
    # company_folder = check_and_create_folder(f'\{company}')
    # os.chdir(company_folder)
    get_balance_sheet.default_sheet(default_location, column_name="Cash")
    get_balance_sheet.default_sheet(default_location, column_name="Total Current Assets")
    # get_balance_sheet.default_balance_sheet(default_location, column_name="Long Term Investments")
    # get_balance_sheet.default_balance_sheet(default_location, column_name="Short Term Investments")
    get_balance_sheet.default_sheet(default_location, column_name="Long Term Debt")
    get_balance_sheet.default_sheet(default_location, column_name="Total Assets")
    get_balance_sheet.default_sheet(default_location, column_name="Total Liab")


def create_quarterly_balance_sheet_charts(company, quarterly=None):
    get_balance_sheet = create_plots.Informations(company, exported_info_folder, "quarterly_balance_sheet")
    print(f"Creating plot to see Quarterly Balance Sheet details about {company}")
    # company_folder = check_and_create_folder(f'\{company}')
    # os.chdir(company_folder)
    get_balance_sheet.default_sheet(default_location, quarterly=True, column_name="Cash")
    get_balance_sheet.default_sheet(default_location, quarterly=True, column_name="Total Current Assets")
    # get_balance_sheet.default_balance_sheet(default_location, column_name="Long Term Investments")
    # get_balance_sheet.default_balance_sheet(default_location, column_name="Short Term Investments")
    get_balance_sheet.default_sheet(default_location, quarterly=True, column_name="Long Term Debt")
    get_balance_sheet.default_sheet(default_location, quarterly=True,  column_name="Total Assets")
    get_balance_sheet.default_sheet(default_location, quarterly=True, column_name="Total Liab")


def create_dividend_chart(company):
    get_info_cashflow = create_plots.Informations(company, exported_info_folder, "cashflow")
    print(f"Creating plot to see CashFlow details about {company}")
    # company_folder = check_and_create_folder(f'\{company}')
    # os.chdir(company_folder)
    get_info_cashflow.default_sheet(default_location, column_name="Dividends Paid")


def create_all_charts(company):
    create_financial_charts(company)
    create_balance_sheet_charts(company)


def create_quarterly_charts(company):
    create_quarterly_balance_sheet_charts(company)
    create_quarterly_financial_charts(company)


def get_recommendations(company):
    get_recommendations = recommendations.Recommendations(company, exported_info_folder)
    get_recommendations.get_recommendations_df()


def get_historical_data(default_location):
    historical_data = get_historical_market_data.GetHistoricalData(company, default_location)
    historical_data.get_historical_data()

if __name__ == '__main__':
    company = "HPQ"
    print(f'Creating the structure folders...')
    create_structure(company)

    # check_and_create_folder(exported_photos_folder + '\\' + company)
    get_historical_data(default_location)
    create_info_files(company)
    get_main_info(company)
    create_main_image(company)
    create_all_charts(company)
    create_quarterly_charts(company)
    create_dividend_chart(company)
