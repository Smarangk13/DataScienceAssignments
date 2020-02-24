# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os

ticker='klm-data'
# input_dir = r'C:\Users\epinsky\bu\python\data_science_with_Python\datasets'
ticker_file = os.path.join(ticker + '.csv')

try:   
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)
    """    your code for assignment 1 goes here
    """
    days = []
    openIndex = 1
    adjCloseIndex = 5
    for line in lines:
        days.append(line.split(','))

    prevClose = days[1][adjCloseIndex]
    profit = 100
    for i in range(2,len(days)):
        if prevClose > days[i][openIndex]:
            # buy
            pass
        elif prevClose > days[i][openIndex]:
            # sell
            pass
        prevClose = days[i][adjCloseIndex]
        

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)












