import pandas as pd
import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt


def scale(nums, numMax, numMin, newMin=0, newMax=1):
    # res = []
    # for n in nums:
    r = (nums - numMin)
    r *= ((newMax - newMin) / (numMax - numMin))
    r += newMin
    # res.append(r)
    return r


fileName = "KOLabels.csv"
df = pd.read_csv(fileName)

# print(days)
meanRange = df['Mean'].max(), df['Mean'].min()
SDRange = df['SD'].max(), df['SD'].min()
print(df.head())
print(meanRange)
meanList = list(df['Mean'])

meanList = scale(meanList,meanRange[0], meanRange[1], 0, 1,)
sdList = scale(list(df['SD']),SDRange[0],SDRange[1])
# print(df.head())
print(meanList)
