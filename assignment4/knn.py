import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


fileName = "KOLabels.csv"
df = pd.read_csv(fileName)

x0 = [[0.2,0.2],[0.1,0.2],[0.3,0.2],[0.3,0.1],[0.7,0.7],[0.6,0.7],[0.8,0.7],[0.8,0.6]]
y0 = ['q3','q3','q3','q3','q1','q1','q1','q1']
knn3 = KNeighborsClassifier(n_neighbors=3)
knn3.fit(x0,y0)
print(knn3.predict([[0.3,0.3]]))