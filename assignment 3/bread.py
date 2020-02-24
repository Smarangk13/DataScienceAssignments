import os
import pandas as pd
import numpy as np

fileName = "Breadbasket_DMS_output.csv"
df = pd.read_csv(fileName)

# 1
print('Question 1')
# Hour
hourly = df.groupby('Hour')['Transaction'].nunique()
print('The busiest hour is ', hourly.idxmax(), ' with ', hourly.max(), 'transactions')

# Day
daily = df.groupby('Weekday')['Transaction'].nunique()
print('The busiest day is ', daily.idxmax(), ' with ', daily.max(), 'transactions')

# Period
timely = df.groupby('Period')['Transaction'].nunique()
print('The busiest period is ', timely.idxmax(), ' with ', timely.max(), 'transactions')

# 2
print('\nQuestion 2')
# Hour
hourly = df.groupby('Hour')['Item_Price'].sum()
print('The most profitable hour is ', hourly.idxmax(), ' earning ', hourly.max())

# Day
daily = df.groupby('Weekday')['Item_Price'].sum()
print('The most profitable day is', daily.idxmax(), ' earning ', daily.max())

# Time
timely = df.groupby('Period')['Item_Price'].sum()
print('The most profitable part of the day is', timely.idxmax(), ' earning ', timely.max())

# 3
print('\nQuestion 3')
populars = df.groupby('Item')['Transaction'].nunique()
print('The most popular item is',populars.idxmax(), 'which sold', populars.max())
print('The least popular item is',populars.idxmin(),'which sold',populars.min())

