'''
This script is to build a table whose columns are closing stock prices of S&P500. Each row of the table represents
stock prices of the same date.
'''
import pandas as pd
df_tickers_list = pd.read_csv('Data/Stocks_in_S&P500/tickers_list.csv')

'''
df_ticker = pd.read_csv('Data/Stocks_in_S&P500/A.csv')
dates_list = []
for date in df_ticker['datetime']:
    dates_list.append(date)
prices_list = []
for price in df_ticker['price']:
    prices_list.append(price)
print(dates_list, prices_list)
'''

def fetch_stock_prices(csv_file_name):
    df_ticker = pd.read_csv('Data/Stocks_in_S&P500/'+ csv_file_name)
    dates_list = []
    for date in df_ticker['datetime']:
        dates_list.append(date)
    prices_list = []
    for price in df_ticker['close']:
        prices_list.append(price)
    return (dates_list, prices_list)


price_list = []
for ticker in df_tickers_list['ticker']:
    print(ticker)
    price_list.append({ticker: fetch_stock_prices(ticker + '.csv')})
print(price_list)







