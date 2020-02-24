import os
import sys
import pandas as pd
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

# Question 1
print()
print("Question 1")
days = []
for line in lines:
    days.append(line.split(','))

positiveDays = 0
negativeDays = 0
returnIndex = 13

for i in days[2:]:
    if float(i[returnIndex]) > 0:
        positiveDays += 1
    else:
        negativeDays += 1

print("positive days = ", positiveDays)
print("negative days = ", negativeDays)

# Question 2
print()
print("Question 2")
total = 0
avg = 0
tradingDays = 0
year = days[1][1]

results = pd.DataFrame(columns=['year', 'trading days', 'mean', '% days < mean', '% days > mean'])

yearStart = 1

for i in range(1, len(days)):
    cyear = days[i][1]
    dailyReturn = float(days[i][returnIndex])
    if cyear == year:
        total += dailyReturn
        tradingDays += 1

    elif cyear != year or i == len(days) - 1:
        avg = total / tradingDays
        hiDays = 0
        for j in range(yearStart, i):
            dailyReturn = float(days[j][returnIndex])
            if dailyReturn > avg:
                hiDays += 1

        lowDays = tradingDays - hiDays
        hiPct = (hiDays / tradingDays) * 100
        lowPct = 100 - hiPct

        results = results.append(pd.Series([year, tradingDays, avg, lowPct, hiPct], index=results.columns),
                                 ignore_index=True)

        year = cyear
        total = 0
        tradingDays = 0
        yearStart = i

print(results)

# Question 3
print()
print("Question 3")
total = 0
avg = 0
tradingDays = 0
year = days[1][1]

results = pd.DataFrame(columns=['year', 'trading days', 'mean', 'SD', '% days < 2mean', '% days > 2mean'])
outboundYears = pd.DataFrame(columns=['year', '% out of bound'])
yearStart = 1

for i in range(1, len(days)):
    cyear = days[i][1]
    dailyReturn = float(days[i][returnIndex])
    if cyear == year:
        total += dailyReturn
        tradingDays += 1

    elif cyear != year or i == len(days) - 1:
        avg = total / tradingDays

        sigma = 0
        for j in range(yearStart, i):
            dailyReturn = float(days[j][returnIndex])
            sigma += (dailyReturn - avg) ** 2

        sd = (sigma / tradingDays) ** 0.5

        upperBound = avg + 2 * sd
        lowerBound = avg - 2 * sd

        hiDays = 0
        lowDays = 0
        for j in range(yearStart, i):
            dailyReturn = float(days[j][returnIndex])
            if dailyReturn > upperBound:
                hiDays += 1

            elif dailyReturn < lowerBound:
                lowDays += 1

        hiPct = (hiDays / tradingDays) * 100
        lowPct = (lowDays / tradingDays) * 100
        outBound = hiPct + lowPct

        results = results.append(pd.Series([year, tradingDays, avg, sd, lowPct, hiPct], index=results.columns),
                                 ignore_index=True)

        outboundYears = outboundYears.append(pd.Series([year, outBound], index=outboundYears.columns),
                                             ignore_index=True)
        year = cyear
        total = 0
        tradingDays = 0
        yearStart = i

print(results)
print(outboundYears)
print('The is mostly a normal distribustion here, the biggest outliers are 2014 and 2017')
