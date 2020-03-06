import pandas as pd
import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt


def scale(nums, numMax, numMin, newMin=0, newMax=1):
    res = []
    for n in nums:
        r = (nums - numMin)*((newMax - newMin) / (numMax - numMin))
        r += newMin
        res.append(r)
    return res


def meanSDRanges(data):
    # print(days)
    meanRange = data['Mean'].max(), data['Mean'].min()
    SDRange = data['SD'].max(), data['SD'].min()
    meanList = list(data['Mean'])

    meanList = scale(meanList,meanRange[0], meanRange[1], 0, 1,)
    sdList = scale(list(data['SD']),SDRange[0],SDRange[1])
    # print(df.head())
    # print(meanList)
    return meanList,sdList

fileName = "KOLabels.csv"
df = pd.read_csv(fileName)

# Setup
df2018 = df[:53]
df2019 = df[53:]

df2018Good = df2018['Label'] == 'Good'
df2019Good = df2019['Label'] == 'Good'
df2018Bad = df2018['Label'] == 'Bad'
df2019Bad = df2019['Label'] == 'Bad'

mean2018Good,sd2018Good = meanSDRanges(df2018[df2018Good])
mean2018Bad,sd2018Bad = meanSDRanges(df2018[df2018Bad])
mean2019Good,sd2019Good = meanSDRanges(df2019[df2019Good])
mean2019Bad,sd2019Bad = meanSDRanges(df2019[df2019Bad])

# Part 1
fig2018 = plt.figure()
pl2018 = fig2018.add_subplot(111)
pl2018.scatter(mean2018Good,sd2018Good, c='green')
pl2018.scatter(mean2018Bad,sd2018Bad, c='red')
p0 = [0.5,0]
p1 = [0,0.5]
pl2018.plot(p0,p1)
plt.show()

# Part 2
fig2019 = plt.figure()
pl2019 = fig2019.add_subplot(111)
pl2019.scatter(mean2019Good,sd2019Good, c='green')
pl2019.scatter(mean2019Bad,sd2019Bad, c='red')
plt.show()

print('Refer pdf for discussion')
