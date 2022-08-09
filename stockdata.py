import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt

import yfinance as yf


def stockHistory(name):
    stock = yf.Ticker(name)
    data = name.history()
    stockdata = data.loc[:, "Open"]
    return stockdata


if __name__ == "__main__":
    print('hello')
"""
plt.figure(figsize=(16, 8))
plt.title('Close Price History', fontsize=18)
plt.plot(intc['Adj Close'])
plt.plot(amd['Adj Close'])
plt.legend(['INTC', 'AMD'], loc='upper left', fontsize=18)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.show()
"""
