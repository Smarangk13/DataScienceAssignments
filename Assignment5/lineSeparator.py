import pandas as pd
import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt

def scale(nums, numMax, numMin, newMin=0, newMax=1):
    r = (nums - numMin)*((newMax - newMin) / (numMax - numMin))
    return r

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


def pointPrinter(data, anotate=True):
    dfGood = data['Label'] == 'Good'
    dfBad = data['Label'] == 'Bad'

    meanGood, sdGood = meanSDRanges(data[dfGood])
    meanBad, sdBad = meanSDRanges(data[dfBad])

    fig = plt.figure()
    pl = fig.add_subplot(111)
    pl.scatter(meanGood, sdGood, c='green')
    pl.scatter(meanBad,sdBad, c='red')

    if not anotate:
        plt.show()
        return fig

    # Annotation
    weeks = list(data[dfGood]['Year-Week'])
    for i in range(len(weeks)):
        lab = weeks[i][5:]
        plt.annotate(lab, (meanGood[i], sdGood[i]))

    weeks = list(data[dfBad]['Year-Week'])
    for i in range(len(weeks)):
        lab = weeks[i][5:]
        plt.annotate(lab, (meanBad[i], sdBad[i]))

    p0 = [0.1, 1]
    p1 = [1, 0.2]
    pl.plot(p0, p1)

    plt.show()
    return pl

fileName = "KOLabels.csv"
df = pd.read_csv(fileName)

# Setup
df2018 = df[:53]
df2019 = df[53:]

# Part 1
fig2018 = pointPrinter(df2018)
