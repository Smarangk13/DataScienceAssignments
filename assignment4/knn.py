import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

fileName = "KOLabels.csv"
df = pd.read_csv(fileName)

df2018 = df[:53]
df2019 = df[53:]


def knnCalc(data, n):
    knn = KNeighborsClassifier(n_neighbors=n)
    labels = np.array(data[['Label']])
    inputData = data[['Mean', 'SD']]

    knn.fit(inputData, labels)
    return knn


def calcAccuracy(test, real):
    count = 0
    for i, x in enumerate(test):
        if x == real[i:i + 1].values:
            count += 1
    res = count / len(real)
    return res

# Setup
knns = {i: knnCalc(df2018, i) for i in range(3, 12, 2)}

accuracy = []
predictions = []
best = 0
bestK = 0
for i, n in enumerate(knns):
    prediction = knns[n].predict(df2019[['Mean', 'SD']])
    predictions.append(prediction)

    score = calcAccuracy(prediction, df2019[['Label']])
    accuracy.append(score)

    if score > best:
        best = score
        bestK = i * 2 + 3

# Question 1
print('\nQuestion 1')
x = [i for i in range(3, 12, 2)]
plt.plot(x, accuracy)
plt.show()

# Question 2
print('\nQuestion 2')
# print(accuracy)
print('The optimal k = ', bestK)

# Question 3
print('\nQuestion 3')
print('Accuracy of optimal k is ', round(accuracy[int((bestK-3)/2)] * 100, 2), '%')

# Question 4
print('\nQuestion 4')
cf = confusion_matrix(list(df2019[['Label']].values), predictions[int((bestK-3)/2)])
print('The confusion matrix appears as - ')
print(cf)

# Question 5
print('\nQuestion 5')
print('The number of  true positives = ', cf[0][0])
print('Sensitivity = ', round(cf[0][0]/len(df2019),2))

# Question 6
print('\nQuestion 6')
print('The number of  true negatives = ', cf[1][1])
print('Specificity = ', round(cf[1][1]/len(df2019), 2))
