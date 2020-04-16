import pandas as pd
from sklearn.linear_model import LinearRegression

fileName = "KOLabels.csv"
df = pd.read_csv(fileName)
df2018 = df[:53]
df2019 = df[53:]


def linearWindow(dfx, w):
    l = len(dfx)
    position = 'None'
    shares = 0
    profit = 0
    nlongs = 0
    nshorts = 0

    for i in range(l - w - 1):
        X = dfx[i:i + w]
        y = dfx[i + 1:i + w + 1]

        LRf = LinearRegression().fit(X, y)
        pw1 = LRf.predict(dfx[i + w:i + w + 1][['Week', 'Close']])
        pw1 = pw[0][1]
        last = dfx.at[i, 'Close']

        if pw1 > last:
            if position == 'None':
                shares = 100 / last
                position = 'long'
                nlongs += 1

            elif position == 'long':
                nlongs += 1

            else:
                px = 100 * shares
                profit += px - pw
                position = 'None'

        elif pw1 < last:
            if position == 'None':
                position = 'short'
                shares = 100 / last
                nshorts += 1


            elif position == 'short':
                nshorts += 1

            else:
                px = last * shares
                profit += px - pw
                position = 'None'

    return profit, nshorts, nlongs

best = 1
max = 0
for i in range(5,30):
    res = linearWindow(df2018,i)
    if res > max:
        max = res
        best = i

print('Best window is',i)
print('Profit for this window is', max[0])
print('Number of shorts positions = ',max[1],'Number of ling positions = ', max[2])

print('\nFor 2019')
res = linearWindow(df2019,best)
print('Profit for 2019 is', res[0])
print('Number of shorts positions = ',res[1],'Number of ling positions = ', res[2])
