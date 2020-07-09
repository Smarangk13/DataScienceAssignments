import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

fileName = "KOLabels.csv"
df = pd.read_csv(fileName)
df2018 = df[:53]
df2019 = df[53:]

gnb = GaussianNB()

X_train = df2018[['Mean','SD']]
y_train = df2018[['Label']]

gnb.fit(X_train, y_train)

y_pred = gnb.predict(df2019[['Mean','SD']])

cf = confusion_matrix(df2019['Label'], y_pred)
tn, fp, fn, tp  = cf.ravel()

#Question 1
print('Question 1')
accuracy = (tp+tn)/len(df2019)*100
print('Accuracy = ','{0:.2f}'.format(accuracy),'%')

#Question 2
print('\nQuestion 2')
print(cf)

#Question 3
print('\nQuestion 3')
print('True positive rate =','{0:.2f}'.format(tp/len(df2019)*100),'%')
print('True negative rate =','{0:.2f}'.format(tn/len(df2019)*100),'%')

#Question 4
print('\nQuestion 4')
df2019New = df2019
df2019New['Label'] = y_pred

buyHold = df2019[:1]['Close']- df2019[-1:]['Close'] * 100

# label trade
position = None
money = 100
shares = 0
totalBalance = 0
for index, row in df2019New.iterrows():
    label = row['Label']
    if label == 'Good':
        if position == None:
            shares = money / float(row['Close'])
            position = 'Hold'
    else:
        if position == 'Hold':
            money = shares * float(row['Close'])
            position = None

    totalBalance += money

totalBalance += shares * float(df2019New[-1:]['Close'])

print('Buy and Hold profit = ',buyHold)
print('Trading based on new labels =',totalBalance-100)