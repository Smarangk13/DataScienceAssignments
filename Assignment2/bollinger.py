import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = 'KO'
# input_dir = r'C:\Users\epinsky\bu\python\data_science_with_Python\datasets'
ticker_file = os.path.join(ticker + '.csv')

try:
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)
    sys.exit()

# Start
days = []
for line in lines:
    days.append(line.split(','))

# Question 1
print()
print("Question 1")


def getSD(nums, avg):
    total = 0
    for n in nums:
        total += (n - avg) ** 2

    sd = total / len(nums)
    sd = sd ** 0.5
    return sd


def bollinger(W, k, data, year):
    openIndex = 7
    closingPriceIndex = 10
    yearIndex = 1
    position = 'none'
    # Implement a queue to hold moving average numbers
    MAq = [0 for i in range(W)]
    pos = 0
    sd = 0

    # Calculate the initial moving average
    i = 1
    while int(data[i][yearIndex]) != year:
        i += 1

    j = i - W
    total = 0
    while j < i:
        closePrice = float(data[j][closingPriceIndex])
        MAq[pos] = closePrice
        total += closePrice
        j += 1
        pos += 1
        pos %= W

    MA = total / W
    sd = getSD(MAq, MA)

    # Calculate P/L for year
    totalProfit = 0
    transactions = 0
    sharesOwned = 0

    i += 1
    while int(data[i][yearIndex]) == year:
        closePrice = float(data[i][closingPriceIndex])

        MA = ((MA * W) - MAq[(pos - 1) % W] + closePrice) / W
        MAq[pos] = closePrice
        pos = (pos + 1) % W
        sd = getSD(MAq, MA)

        bandUpper = MA + k * sd
        bandLower = MA - k * sd
        if closePrice > bandUpper:
            if position == 'none':
                # Short sell(buy 100 worth)
                position = 'short'
                sharesOwned = 100 / closePrice

            elif position == 'short':
                # Do nothing
                pass

            # position = long
            else:
                # Sell shares
                position = 'none'
                sold = sharesOwned * closePrice
                profit = sold - 100
                totalProfit += profit
                transactions += 1

        elif closePrice < bandLower:
            if position == 'none':
                # buy 100 at closing price
                position = 'long'
                sharesOwned = 100 / float(data[i][openIndex])

            elif position == 'long':
                # do nothing
                pass

            # position = short
            else:
                position = 'none'
                # buy back shares
                bought = sharesOwned * float(data[i][openIndex])
                profit = 100 - bought
                totalProfit += profit
                transactions += 1

        i += 1

    avgProfit = 0

    if transactions != 0:
        avgProfit = totalProfit / transactions

    return avgProfit


# Q1 for different w,k
def ranger(year, data):
    x = []
    y = []
    colors = []
    areas = []
    ks = [0.5, 1, 1.5, 2, 2.5]
    maxProfit = 0
    bestCombo = 0,0
    for W in range(10, 51):
        eachKW = []
        for k in ks:
            profit = bollinger(W, k, data, year)
            x.append(k)
            y.append(W)
            areas.append(abs(profit * 20))
            if profit > 0:
                colors.append('green')
            else:
                colors.append('red')

            if profit > maxProfit:
                maxProfit = profit
                bestCombo = W,k

    plt.scatter(x, y, areas, colors, alpha=0.5)
    plt.show()
    return bestCombo


# Question 2
print()
print('Question 2')
print('Best combination for 2017 fow W,K = ', ranger(2017, days))
print('We can see that the returns increase by increasing the window upto a certain point, and that the wider bands '
      'generally give a bigger return until the point it stops being viable. This is because no transactions will '
      'occur if the band is too wide')

# Question 3
print()
print('Question 3')
print('Best combination for 2017 fow W,K = ', ranger(2018, days))

print('In 2018 there was a big drop in the prices for coca cola, this made tge stock fluctuate more causing a bigger '
      'standard deviation. This is why we can see bigger bubbles on the right side for this graph')
