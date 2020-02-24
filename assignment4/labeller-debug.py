import pandas as pd
import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt

ticker = "KO.csv"

with open(ticker) as f:
    lines = f.read().splitlines()
print('opened file for ticker: ', ticker)

# Start
days = []
for line in lines:
    days.append(line.split(','))

# print(days)
yearIndex = 1
yearWeekIndex = 6
openIndex = 7
highIndex = 8
lowIndex = 9
closeIndex = 10
volIndex = 11

i = 1
while days[i][yearIndex]!='2018':
    i += 1

days2018 = days[i:]
print(days2018)

def calculateSD(nums,mean):
    s = 0
    for n in nums:
        s += (mean-n)**2
    r = (s/len(nums))**0.5
    return r

weeks = []
currentWeek = days2018[0][yearWeekIndex]
vol = 0
wO = float(days2018[0][openIndex])
wC = 0
wH = 0
wL = 1000
totalVol = 0
weekStart = 0
weekEnd = 0
weeklyReturn = 0
returnArray = []

for i,day in enumerate(days2018):
    yearWeek = day[yearWeekIndex]
    if currentWeek == yearWeek:
        # Calculate total volume
        vol += float(day[volIndex])
        totalVol += vol
        
        # Calculate weekey mean
        dailyReturn = float(day[closeIndex]) - float(day[openIndex])
        weeklyReturn += dailyReturn
        returnArray.append(dailyReturn)
        
        # Get Weekly High and low
        if float(day[highIndex]) > wH:
            wH = float(day[highIndex])
            
        if float(day[lowIndex]) < wL:
            wL = float(day[lowIndex])
            
    else:
        # Caclulate weekly mean and SD
        weekEnd = i
        weekMean = weeklyReturn/(weekEnd - weekStart)
        if currentWeek == '2018-51':
            print('ok')
        if len(returnArray)==0:
            print('weekNo = ',currentWeek)
            sd = 0
        else:
            sd = calculateSD(returnArray,weekMean)
        returnArray = []
        weekStart = i
        
        # Format week table
        wC = float(days2018[i-1][closeIndex])
        week = []
        # week = [currentWeek, wO, wC, wH, wL, vol]
        week.append(currentWeek)
        week.append(wO)
        week.append(wC)
        week.append(wH)
        week.append(wL)
        week.append(vol)
        week.append(weekMean)
        week.append(sd)
        
        # print(week)
        currentWeek = yearWeek
        wO = float(day[openIndex])
        vol = 0
        wH = float(day[highIndex])
        wL = float(day[lowIndex])
        weeks.append(week)
        weekMean = 0

for week in weeks:
    if week[2] > week[1]:
        week.append('Good')
        continue
    week.append('Bad')

print(weeks)

print('Year-Week,Open,Close,High,Low,Volume,Label')
for week in weeks:
    res = ''
    for i in week:
        res += str(i)+','
    print(res[:-1])
