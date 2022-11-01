# BeforeInvesting

BeforeInvesting is a project that gave me the opportunity to learn a little bit more about how to use OOP and how to automate different processes.

Scope

I developed these scripts to help me find informations about the companies listed on the New York Exchange Market.

How it works

The main script needs a parameter for input and the parameter must be company's sticker symbol (ex: AAPL).
I extract the data using yfinance library into csv and json files for that company and I create different visualizations in order to get an overview of the company.

The files will be in the "exported_info" folder and the visualizations will be in the "exported_photos" folder.

A folder will be created for each company, if a company folder already exists, the information will be overwritten.

The visualizations are divided in 2 parts:
1. The main photo - where General Information can be found (ex: Current Price, Market Cap, Total Revenue, Free CashFlow, Margins, Stock Price Targets, Stock Price Evolution etc). See below picture:

![image](https://user-images.githubusercontent.com/40692414/199305054-b30d26a7-85df-4854-aa36-a26cde426625.png)

2. Different photos - where Stock Historical Price Evolution can be found, company's Balance Sheet for the last 4 years, Net income etc.)

![image](https://user-images.githubusercontent.com/40692414/199305158-23d3f3e5-1424-4b82-9e6b-8336c90cfb52.png)


Because this information is very useful to me, I thought that other people may be interested, so I created an Instagram Account where I share all this information. It's not much work to do because all the steps are automated, I just insert a ticker symbol as a parameter and after 10-20seconds I have all the information I need.

The outputs are not very pretty and that's why I've put the same informations in a PowerBI Project and I created some visualizations that I found to be more easier to read.
