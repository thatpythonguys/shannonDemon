from random import randint, seed
import matplotlib.pyplot as plt
import numpy as np
#print(randint(0,1))

#print( 3 /2)
"""
plot_size = plt.rcParams["figure.figsize"]
print(plot_size[0])
print(plot_size[1])

plt.plot([-3,-2,-1,0,1,2,3],[9,4,1,0,1,4,9])
plt.show()
"""
seed(2)

#stockAmounts = [cash, stock1, stock2, stock3]
class portfolio:
    def __init__(self, stockAmounts, desiredAllocation):
        self.stockAmounts = stockAmounts
        self.totalvalue = self.totalValue()
        #this can later be generalized to a list of stocks and their respective stockAmountss
        #self.cash = (1 - stockAmounts) * totalvalue
        self.cash = stockAmounts[0][1] #0th column is the name, 1st column is the amount of stock

    def totalValue(self):
        curVal = 0
        for stock in self.stockAmounts:
            if stock[0] == "cash":
                curVal += stock[1] # for the cash row, the name is cash and the "amount of stock" is just the amount of cash
        curVal += stock[1] * stock[0].value
        return curVal

    def rebalance(self):
        self.totalvalue = self.totalValue()
        self.stockAmounts[0][1] = self.totalvalue * desiredAllocation[0][1] #for the cash
        for i in range(1, len(self.stockAmounts)):
            self.stockAmounts[i][1] = self.totalvalue * desiredAllocation[i][1] / (self.stockAmounts[i][0].value)

    def printInfo(self):
        print("Current Distribution:")
        for stock in self.stockAmounts:
            if stock[0] == "cash":
                print(stock[1], "cash")
            else:
                print(stock[1], stock[0].name)


class stock:
    def __init__(self, name, value):
        self.name = name
        self.value  = value #initial value

    #behavior function
    def stockChange(self):
        if randint(0,1) == 1:
            self.value = self.value * 2
        else:
            self.value = self.value / 2
        return self.value

msft = stock("msft", 100)
aapl = stock("aapl", 100)
InitialstockList = [["cash", 100],[aapl, 200]]
#desiredAllocation = [['cash', 0.2], [aapl, 0.5], [msft, 0.3]]
desiredAllocation = [['cash', 0.5], [aapl, 0.5]]

p1 = portfolio(InitialstockList, desiredAllocation)
print("MSFT Price is now", msft.value)
print("AAPL Price is now", aapl.value)
print("Current Portfolio Value is:", p1.totalvalue)

p1.printInfo()

print("\nThe Next Day...")
msft.stockChange()
aapl.stockChange()

print("MSFT Price is now", msft.value)
print("AAPL Price is now", aapl.value)
p1.rebalance()

p1.printInfo()
