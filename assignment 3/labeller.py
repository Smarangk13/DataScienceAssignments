#!/usr/bin/env python
# coding: utf-8

# In[33]:


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


# In[34]:


# print(days)
yearIndex = 1
yearWeekIndex = 6
openIndex = 7
highIndex = 8
lowIndex = 9
closeIndex = 10
volIndex = 11


# In[36]:


i = 1
while days[i][yearIndex]!='2018':
    i += 1

days2018 = days[i:]
print(days2018)


# In[43]:


weeks = []
currentWeek = days2018[0][yearWeekIndex]
vol = 0
wO = float(days2018[0][openIndex])
wC = 0
wH = 0
wL = 1000
totalVol = 0

for i,day in enumerate(days2018):
    yearWeek = day[yearWeekIndex]
    if currentWeek == yearWeek:
        vol += float(day[volIndex])
        totalVol += vol
        if float(day[highIndex]) > wH:
            wH = float(day[highIndex])
            
        if float(day[lowIndex]) < wL:
            wL = float(day[lowIndex])
            
    else:
        wC = float(days2018[i-1][closeIndex])
        week = []
        # week = [currentWeek, wO, wC, wH, wL, vol]
        week.append(currentWeek)
        week.append(wO)
        week.append(wC)
        week.append(wH)
        week.append(wL)
        week.append(vol)
        
        # print(week)
        currentWeek = yearWeek
        wO = float(day[openIndex])
        vol = 0
        wH = float(day[highIndex])
        wL = float(day[lowIndex])
        weeks.append(week)

# print(weeks)


# In[45]:


for week in weeks:
    if week[2] > week[1]:
        week.append('Good')
        continue
    week.append('Bad')

print(weeks)


# In[ ]:




