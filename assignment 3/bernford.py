import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'online_retail.csv'
df = pd.read_csv(file)

model1 = [0.1 for i in range(1, 10)]
model2 = [math.log10(1+1/i) for i in range(1, 10)]

realCount = [0 for i in range(1,10)]
for i in df['UnitPrice']:
    first = str(i)[0]
    if first == '0':
        first = str(i)[2]
    realCount[int(first)-1] += 1
real = [round(i/len(df),2) for i in realCount]

# 1
print('Question 1')
print('See Graph')
# print(real)
# x = [i for i in range(1,10)]
x = np.array(range(1,10))
width = 0.25
buffer = 0.05
box = plt.subplot(1, 1, 1)
equalPlot = box.bar(x, model1, width, color='black')
BernPlot = box.bar(x + width + buffer, model2, width, color='green')
realPlot = box.bar(x + width * 2 + buffer * 2, real, width, color='red')

box.set_ylabel('Frequency %')
box.set_xticks(x + width)
box.set_xticklabels(x)
box.legend((equalPlot[0], BernPlot[0], realPlot[0]), ('Equal Weight', 'Bernford', 'Real'))

plt.show()

# 2
print('\nQuestion 2')
print('See Graph')

errorM1 = [abs(model1[i]-real[i]) for i in range(9)]
errorM2 = [abs(model2[i]-real[i]) for i in range(9)]

width = 0.4
buffer = 0.05
box = plt.subplot(1, 1, 1)
equalPlot = box.bar(x, errorM1, width, color='black')
BernPlot = box.bar(x + width+buffer, errorM2, width, color='green')

box.set_ylabel('Absolute error')
box.set_xlabel('Digit')
box.set_xticks(x + width)
box.set_xticklabels(x)
box.legend((equalPlot[0], BernPlot[0]), ('Equal Weight', 'Bernford'))

plt.show()

# 3
print('\nQuestion 3')
sum1 = 0
sum2 = 0
for i in range(9):
    sum1 += errorM1[i]**2
    sum2 += errorM2[i] ** 2

rmse1 = round((sum1/10) ** 0.5, 2)
rmse2 = round((sum2/10) ** 0.5, 2)

print('RMS Error in model 1 = ', rmse1)
print('RMS Error in model 2 = ', rmse2)

# 4
print('\nQuestion 4')
print('We can see from the graphs that the Bernford model appears close to the real distribution. This can also be '
      'seen in the second graph because in most cases the result from the Bernford is closer to 0 than the equal '
      'distribution. \nFinally, the RMS error for the Bernford distribution is lower, this means that it is a better '
      'model for predicting the first digit')
