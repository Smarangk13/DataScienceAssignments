import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn import preprocessing

fileName = "KOLabels.csv"
df = pd.read_csv(fileName)

x = df[['Mean','SD']].values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df[['Mean','SD']] = pd.DataFrame(x_scaled)

df2018 = df[:53]
df2019 = df[53:].reset_index(drop = True)

kmeans = KMeans(n_clusters = 3, random_state = 0)

X_train = np.array(df2018[['Mean','SD']])
kmeans.fit(X_train)

#Question 1
print('Question 1')
distortions = []
kModels = []
for k in range(1,9):
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(X_train)
    kModels.append(kmeanModel)
    distortions.append(sum(np.min(cdist(X_train, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X_train.shape[0])


# Plot the elbow
plt.plot([k for k in range(1,9)], distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The knee shaped graph')
plt.show()

print('We can see that the best k is 3 or 4, we will take 4')

k = 4
reds = [0 for i in range(k)]
greens = [0 for i in range(k)]

# Question 2
print('\nQuestion 2')
kmeanModel = kModels[k-1]

for i in range (len(df2019)):
    x = np.array(df2019[i:i+1][['Mean','SD']])
    close = kmeanModel.predict(x)
    
    close = int(close)
    if df2019.at[i,'Label'] == 'Good':
        reds[close] += 1
    else:
        greens[close] += 1
    
redPercents = []
greenPercents = []
for i in range(k):
    res = '0'
    if (greens[i]+reds[i]) != 0:
        res = reds[i]/(greens[i] + reds[i]) * 100
        '{0:.2f}'.format(res)
        greenPercents.append('{0:.2f}'.format(100-res))
    else:
        greenPercents.append(res)
    redPercents.append(res)

results = pd.DataFrame(columns = ['Greens Percentage','Reds Percentage'])
results['Greens Percentage'] = greenPercents
results['Reds Percentage'] = redPercents
print(results)

# Question 3
print('\nQuestion 3')
print('None of the clusters have a pure disctribution of red or green')
print('Note:- Cluster 0 has no elements because of the difference in shapes of graphs of 2018 and 2019')


# In[ ]:




