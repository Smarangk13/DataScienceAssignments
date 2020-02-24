#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
import matplotlib.pyplot as plt

ticker = 'KO'
# input_dir = r'C:\Users\epinsky\bu\python\data_science_with_Python\datasets'
ticker_file = os.path.join(ticker + '.csv')

# In[2]:


try:
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)


except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)
    sys.exit()

# In[3]:


"""    your code for assignment 1 goes here
    """
days = []
for line in lines:
    days.append(line.split(','))

# In[4]:


openIndex = 7
adjCloseIndex = 12
longProfit = []
longTotal = 0
shortProfit = []
shortTotal = 0


# In[5]:

def longBuy(prevValue, openValue, closeValue, trsh=0):
    stocks = 0
    perReturn = (openValue - prevValue) / prevValue * 100.00
    if perReturn > trsh:
        purchase = 100
        stocks = purchase / openValue
        sales = stocks * closeValue
        profit = sales - purchase

        return profit

    else:
        return 0


# In[6]:


def shortSell(prevValue, openValue, closeValue, trsh=0):
    stocks = 0
    if (prevValue - openValue) / prevValue * 100 > trsh:
        sell = 100
        stocks = sell / openValue
        buy = stocks * closeValue
        profit = sell - buy

        # per share profit/loss
        #         pershare = openValue - closeValue
        return profit

    else:
        return 0


# In[7]:


prevClose = days[1][adjCloseIndex]

profit = 100
for i in range(2, len(days)):
    if prevClose < days[i][openIndex]:
        moneyMade = longBuy(float(prevClose), float(days[i][openIndex]), float(days[i][adjCloseIndex]))
        longTotal += moneyMade
        longProfit.append(moneyMade)

    elif prevClose > days[i][openIndex]:
        moneyMade = shortSell(float(prevClose), float(days[i][openIndex]), float(days[i][adjCloseIndex]))
        shortTotal += moneyMade
        shortProfit.append(moneyMade)

    prevClose = days[i][adjCloseIndex]

# In[25]:


print(longTotal, shortTotal)
# print(longProfit)
# print(len(days), len(longProfit), len(shortProfit))
print("long avg = ",longTotal/len(longProfit))
print("short avg = ",shortTotal/len(shortProfit))
# In[ ]:

print("tresh test")
longProfit = []
longTotal = 0
shortProfit = []
shortTotal = 0
maxTotal = -1000000000
opt = 0
totalHist = []
longavg = []
shortavg = []
for t in range(0,100):
    tresh = float(t/100)
    for i in range(2, len(days)):
        if prevClose < days[i][openIndex]:
            moneyMade = longBuy(float(prevClose), float(days[i][openIndex]), float(days[i][adjCloseIndex]),tresh)
            longTotal += moneyMade
            longProfit.append(moneyMade)

        elif prevClose > days[i][openIndex]:
            moneyMade = shortSell(float(prevClose), float(days[i][openIndex]), float(days[i][adjCloseIndex]),tresh)
            shortTotal += moneyMade
            shortProfit.append(moneyMade)

        prevClose = days[i][adjCloseIndex]

    total = longTotal + shortTotal
    totalHist.append(total)
    shortavg.append(shortTotal/len(shortProfit))
    longavg.append(longTotal/len(longProfit))
    # print(total)
    if total>maxTotal:
        opt = t
    longProfit = []
    longTotal = 0
    shortProfit = []
    shortTotal = 0

print("optimal = ",opt)
plt.plot(totalHist)
plt.show()
print("short =")
print(shortavg)
plt.plot(shortavg)
plt.show()
print("long =")
print(longavg)
plt.plot(longavg)
plt.show()