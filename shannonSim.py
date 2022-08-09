"""
GOAL: Create a simulation where we rebalance the portfolio 50-50 according to some trigger (time or trigger) and return a graph of the results.

Step 1: Initialize our portfolio - Start with "cash" and "stock"

Step 2: Define how the stock will perform:
            Simple case: stock will double or halve every day.
            Real case: Retrieve real stock data.

Step 4: Run the simulation:
            Parameters: Time of total simulation, trigger for rebalancing

            2 sims: One person who goes "all in" (buys only stock)
                    Other person rebalances periodically

            Return the graph of the simulation
"""
from random import randint, seed
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

seed(5)

# stockHoldings = [[cash, amountofCash], [stock1_name, #shares], [stock2_name, #shares], ...]
# desiredAllocation = [[cash, %allocation], [stock1_name, %allocation]]


class portfolio:
    def __init__(self, stockHoldings, desiredAllocation):
        self.stockHoldings = stockHoldings
        self.totalvalue = self.totalValue()
        self.desiredAllocation = desiredAllocation
        # this can later be generalized to a list of stocks and their respective stockHoldings
        #self.cash = (1 - stockHoldings) * totalvalue
        # 0th column is the name, 1st column is the amount of stock
        self.cash = stockHoldings[0][1]

    def totalValue(self):  # calculates current value of portfolio.
        curVal = 0
        for stock in self.stockHoldings:
            if stock[0] == "cash":
                # for the cash row, the name is cash and the "amount of stock" is just the amount of cash
                curVal += stock[1]
        curVal += stock[1] * stock[0].value
        return curVal

    def rebalance(self):  # rebalance according to the proportions identified in desiredAllocation
        self.totalvalue = self.totalValue()
        self.stockHoldings[0][1] = self.totalvalue * \
            self.desiredAllocation[0][1]  # for the cash
        for i in range(1, len(self.stockHoldings)):
            self.stockHoldings[i][1] = self.totalvalue * \
                self.desiredAllocation[i][1] / (self.stockHoldings[i][0].value)

    def printInfo(self):  # print the current holdings in the portfolio
        print("Current Holdings:")
        for stock in self.stockHoldings:
            if stock[0] == "cash":
                print(stock[1], "cash")
            else:
                print(stock[1], stock[0].name)


class fakeStock:  # these stocks behave according to a predertimined function.
    def __init__(self, name, value):
        self.name = name
        self.value = value  # initial value

    # behavior function
    def stockChange(self, day):  # change value of the stock
        if randint(0, 1) == 1:
            self.value = self.value * 2
        else:
            self.value = self.value / 2
        return self.value


class realStock:  # these stocks actually draw from historical data.
    def __init__(self, name):
        self.name = name
        self.stockdata = self.stockHistory(self.name)
        self.value = self.stockdata[0]

    def stockHistory(self, name):
        obj = yf.Ticker(name)
        data = obj.history(period="2yr", interval="1d", start="2018-01-01")
        stockdata = data.loc[:, "Open"]
        return stockdata

    def stockChange(self, day):
        self.value = self.stockdata[day]


# STOCK INITIALIZATION
stocks = []
# fake stocks -------------------
msft = fakeStock("msft", 100)
aapl = fakeStock("aapl", 100)
# desiredAllocation = [['cash', 0.2], [aapl, 0.5], [msft, 0.3]]
# real stocks -------------------
goog = realStock("goog")
# ------------------------------
stocks.append(msft)
stocks.append(aapl)
stocks.append(goog)


# -------------------------------
# PORTFOLIO INITIALIZATION
InitialstockList1 = [["cash", 10], [goog, 20]]
desiredAllocation1 = [['cash', 0.5], [goog, 0.5]]
# this porfolio rebalances to 50% cash and 50% apple.
p1 = portfolio(InitialstockList1, desiredAllocation1)

InitialstockList2 = [["cash", 10], [goog, 20]]
desiredAllocation2 = [['cash', 0], [goog, 1]]
p2 = portfolio(InitialstockList2, desiredAllocation2)

# RUNNING THE simulation

p1Performance = []
p2Performance = []
aaplPrice = []
googPrice = []


def simulation(numDays):  # WORK IN PROGRESS
    for day in range(numDays):
        for stock in stocks:
            stock.stockChange(day)
        aaplPrice.append(aapl.value)
        googPrice.append(goog.value)
        p1.rebalance()
        p1Performance.append(p1.totalValue())
        p2Performance.append(p2.totalValue())


# Main run
simulation(300)
days = [x for x in range(300)]

# print(aaplPrice)
# print(p2Performance)

# Set up plot
plt.plot(days, p1Performance, "purple", label="portfolio one")
plt.plot(days, p2Performance, "blue", label="portfolio two")
#plt.plot(days, aaplPrice, "goldenrod", label="apple")
plt.plot(days, googPrice, "fuchsia", label="Google")
plt.legend()
plt.show()
