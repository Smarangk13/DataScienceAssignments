import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv('KOlabels.csv')

df2018 = df[:53]
df2019 = df[53:]

x = df2018[['Mean','SD']]
y = df2018['Label']
xtest = df2019[['Mean','SD']]

classifier = LogisticRegression(random_state = 0)
classifier.fit(x, y)
y_pred = classifier.predict(xtest)

y2019 = df2019['Label']

cm = confusion_matrix(y2019, y_pred)
print('Confusion Matrix',cm)