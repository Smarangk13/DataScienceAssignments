import matplotlib.pyplot as plt


class customKnn:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def fit(self, X, Labels):
        pass

    def predict(self):
        pass

    def draw_decision_boundary(self):
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
