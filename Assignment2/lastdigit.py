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

#
print()
print("Question 1")
days = []
for line in lines:
    days.append(line.split(','))


def lastDigitAnalysis(days):
    openIndex = 7

    lastDigits = {i: 0 for i in range(0, 10)}
    # predictions = [0.1 for i in range(0, 10)]
    result = []

    for i in days[1:]:
        last = int(i[openIndex][-1])
        lastDigits[last] += 1

    print(lastDigits)

    most = 0
    mostDigit = 0
    least = len(days)
    leastDigit = 0

    for i in lastDigits:
        if lastDigits[i] > most:
            most = lastDigits[i]
            mostDigit = i

        if lastDigits[i] < least:
            least = lastDigits[i]
            leastDigit = i

    # Question 1
    print()
    print('Question 1')
    print('most frequent digit = ', mostDigit)

    # Question 2
    print()
    print('Question 2')
    print('Least  frequent digit = ', leastDigit)

    # Question 3
    print()
    print('Question 3')

    totalDays = len(days) - 1
    maxError = 0
    errors = []
    total = 0
    for i in lastDigits:
        digitPct = lastDigits[i] / totalDays
        result.append(digitPct)

        error = abs(digitPct - 0.1)
        if error > maxError:
            maxError = error

        total += error
        errors.append(error)

    errors.sort()
    mean = total / 10
    median = (errors[4] + errors[5]) / 2
    total = 0
    for e in errors:
        total += e ** 2
    rms = (total / 10) ** 0.5

    print('Max absolute error = ', maxError)
    print('Mean = ', mean)
    print('Median = ', median)
    print('Root mean Square = ', rms)

    return mostDigit, leastDigit, maxError, median, mean, rms


results = pd.DataFrame(columns=['year', 'Most frequent Digit', 'Least frequent Digit', 'Max Error', 'Median error',
                                'Mean error', 'Root Mean Square Error (RMSE)'])
overall = lastDigitAnalysis(days)
overall = ['Overall '] + [n for n in overall]

results = results.append(pd.Series([n for n in overall], index=results.columns),
                         ignore_index=True)

start = 1
year = days[1][1]
for i in range(1, len(days)):
    cyear = days[i][1]
    if cyear != year:
        stats = lastDigitAnalysis(days[start:i])
        stats = [year] + [n for n in stats]
        results = results.append(pd.Series([n for n in stats], index=results.columns),
                                 ignore_index=True)
        year = cyear
        start = i

pd.set_option('display.max_columns', None)
print(results)