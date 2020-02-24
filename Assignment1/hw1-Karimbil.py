#!/usr/bin/env python
# coding: utf-8

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
import sys
import matplotlib.pyplot as plt

ticker = 'KO'
# input_dir = r'C:\Users\epinsky\bu\python\data_science_with_Python\datasets'
ticker_file = os.path.join(ticker + '.csv')


class inertia:
    openIndex = 7
    adjCloseIndex = 12

    def __init__(self, stockData):
        self.stockData = stockData
        pass

    def longBuy(self, prevValue, openValue, closeValue, threshold=0.0):
        stocks = 0
        perReturn = (openValue - prevValue) / prevValue * 100.00
        if perReturn > threshold:
            # Same as 100/open * (close - open)
            purchase = 100
            stocks = purchase / openValue
            sales = stocks * closeValue
            profit = sales - purchase

            return profit

        else:
            return 0

    def shortSell(self, prevValue, openValue, closeValue, threshold=0.0):
        stocks = 0
        if (prevValue - openValue) / prevValue * 100 > threshold:
            sell = 100
            stocks = sell / openValue
            buy = stocks * closeValue
            profit = sell - buy

            return profit

        else:
            return 0

    def inertiaTrade(self, threshold=0.0):
        longProfit = []
        longTotal = 0
        shortProfit = []
        shortTotal = 0

        prevClose = days[1][self.adjCloseIndex]
        for i in range(2, len(self.stockData)):
            if prevClose < self.stockData[i][self.openIndex]:
                moneyMade = self.longBuy(float(prevClose), float(self.stockData[i][self.openIndex]),
                                         float(self.stockData[i][self.adjCloseIndex]), threshold)
                longTotal += moneyMade
                longProfit.append(moneyMade)

            elif prevClose > self.stockData[i][self.openIndex]:
                moneyMade = self.shortSell(float(prevClose), float(self.stockData[i][self.openIndex]),
                                           float(self.stockData[i][self.adjCloseIndex]), threshold)
                shortTotal += moneyMade
                shortProfit.append(moneyMade)

            prevClose = days[i][self.adjCloseIndex]

        return {'longProfit': longProfit, 'longTotal': longTotal,
                'shortProfit': shortProfit, 'shortTotal': shortTotal}


if __name__ == '__main__':
    try:
        with open(ticker_file) as f:
            lines = f.read().splitlines()
        print('opened file for ticker: ', ticker)

    except Exception as e:
        print(e)
        print('failed to read stock data for ticker: ', ticker)
        sys.exit()

    """    your code for assignment 1 goes here
        """
    days = []
    for line in lines:
        days.append(line.split(','))

    trader = inertia(days)
    results = trader.inertiaTrade()

    # Question 1
    print('\nQuestion 1')
    totalProfitAvg = (results['longTotal'] + results['shortTotal']) / len(days)
    print('Daily avg = ', totalProfitAvg)

    # Question 2
    print('\nQuestion 2')
    print('long avg = ', results['longTotal'] / len(results['longProfit']))
    print('short avg = ', results['shortTotal'] / len(results['shortProfit']))

    if results['shortTotal'] > results['longTotal']:
        print('Short Trading is better')

    elif results['shortTotal'] < results['longTotal']:
        print('Long Trading is better')

    else:
        print('Both Positions equally profitable ')

    # Question 3
    print('\nQuestion 3')
    print("Threshold test")

    maxTotal = float('-inf')
    maxShort = float('-inf')
    maxLong = float('-inf')

    opt = 0
    sOpt = 0
    lOpt = 0

    totalHist = []
    longavg = []
    shortavg = []

    t = [i / 10 for i in range(0, 100)]
    for thresh in t:
        results = trader.inertiaTrade(thresh)

        total = (results['longTotal'] + results['shortTotal']) / len(days)
        totalHist.append(total)
        shortavg.append(results['shortTotal'] / len(results['shortProfit']))
        longavg.append(results['longTotal'] / len(results['longProfit']))

        if total > maxTotal:
            opt = thresh
            maxTotal = total

        if results['longTotal'] > maxLong:
            lOpt = thresh
            maxLong = results['longTotal']

        if results['shortTotal'] > maxShort:
            sOpt = thresh
            maxShort = results['shortTotal']

    print("Optimal rate to use = ", opt, "%")

    # Question 3/4
    plt.plot(t, totalHist)
    # plt.show()
    plt.plot(t, longavg)
    # plt.show()
    plt.plot(t, shortavg)
    # plt.show()

    # Question 4
    print('\nQuestion 4')
    print('Optimal for long positions = ', lOpt)
    print('Optimal for short positions = ', sOpt)
    print('For this company we can see that for long buying positions which is more prominent having a higher '
          'threshold reduces our loss ')
    print('For short positions the we appear to stop buying after a certain threshold this makes it more profitable '
          'to buy at lower threshholds')

    plt.show()
