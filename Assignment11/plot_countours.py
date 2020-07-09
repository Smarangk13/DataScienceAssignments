# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 09:55:40 2020

@author: epinsky
"""
# skeleton to draw a decision surface
# note: need to add points - this just draws a decision surface

import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.model_selection import train_test_split

url = r'https://archive.ics.uci.edu/ml/'  + \
           r'machine-learning-databases/iris/iris.data'

iris_feature_names = ['sepal-length', 'sepal-width', 
                                  'petal-length', 'petal-width']
data = pd.read_csv(url, names=['sepal-length', 'sepal-width', 
                                  'petal-length', 'petal-width', 'Class'])

class_labels = ['Iris-versicolor', 'Iris-virginica']
data = data[data['Class'].isin(class_labels)]

x_label = 'sepal-length'
y_label = 'sepal-width'
data_feature_names = [x_label, y_label]

X = data[data_feature_names].values
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

le = LabelEncoder()
Y = le.fit_transform(data['Class'].values)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, 
                                                    random_state=3)

lda_classifier = LDA()
lda_classifier.fit(X_train,Y_train)

knn_classifier = KNeighborsClassifier(n_neighbors=3) 
knn_classifier.fit(X,Y)



def make_meshgrid(x, y, h=.02, delta = 0.05):
    x_min, x_max = (1-delta) * (x.min() - 1), (1+delta) * (x.max() + 1)
    y_min, y_max = (1-delta) * (y.min() - 1), (1+delta) * (y.max() + 1)
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, classifier, xx, yy, **params):
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out



# any classifier here
# classifier = LDA()
classifier = KNeighborsClassifier(n_neighbors=3) 
classifier.fit(X,Y)




fig, ax = plt.subplots()
title = ('Decision surface of classifier ')
# Set-up grid for plotting.
X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)
plot_contours(ax, classifier, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)


plt.show()









