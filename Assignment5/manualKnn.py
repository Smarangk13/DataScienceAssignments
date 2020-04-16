import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.spatial import distance


class customKnn:
    def __init__(self, neighbours_k, parameter_p):
        self.result = 'Bad'
        self.k = neighbours_k
        self.p = parameter_p

    def __str__(self):
        pass

    def fit(self, X, Labels):
        self.df = X
        pass

    def predict(self, new_X):
        if self.p == 1:
            pass

        elif self.p == 1.5:
            pass

        # Minkovski
        else:
            dists = pd.DataFrame(columns=['Dist', 'Label'])
            p1 = [0.4, 0.5]

            for i in range(len(self.df)):
                m, s = float(self.df[i:i + 1]['Mean']), float(self.df[i:i + 1]['SD'])
                p2 = [m, s]
                lab = self.df.at[53 + i, "Label"]
                d = distance.minkowski(p1, p2, 2)
                dists = dists.append({'Dist': d, 'Label': lab}, ignore_index=True)

        sorteddf = dists.sort_values(by='Dist', axis=0)
        knn = sorteddf[:self.k]
        self.knn = knn.reset_index(drop=True)
        self.closeLabels(knn)

    def draw_decision_boundary(self):
        pass

    def closeLabels(self, knn):
        goods = 0
        for i in range(len(knn)):
            lab = knn.at[i, "Label"]
            if lab == "Good":
                print('Good')
                goods += 1

        if goods > len(knn)//2:
            self.result = 'Good'
        else:
            pass


points = [(1, 1), (2, 2), (1, 0), (-1, 1), (-1, -1), (-1, 0), (0, 1), (0, 0), (0.5, 0.5), (0.9, 0.9), (4, 4), (8, 8)]
x = []
y = []
for p in points:
    x.append(p[0])
    y.append(p[1])

plt.scatter(x, y)

plt.show()

circleCentre = (0, 0)
radius = 1

form = lambda x1, y1: (circleCentre[0] - x1) ** 2 + (circleCentre[1] - y1) ** 2 - radius

for p in points:
    print(p, form(p[0], p[1]))
