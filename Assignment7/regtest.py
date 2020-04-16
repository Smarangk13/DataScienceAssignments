import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
X = np.array([[2, 1], [3, 2], [6, 5], [10, 9]])
y = np.array([4,6,12,20])
clf = LinearRegression().fit(X, y)
r = clf.predict(np.array([[4,3]]))
print(X)
print(y)
print(r)

x = {'Date':[1,2,5,10],'Value':[1,2,5,10]}
X = pd.DataFrame(x)
yx = {'Res':[2]}
clf = LinearRegression().fit(X, y)
r = clf.predict(np.array([[4,4]]))
print(X)
print(y)
print(r)

