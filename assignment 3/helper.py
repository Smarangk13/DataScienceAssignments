# This is what I used to label food/drinks

import pandas as pd

file = 'BreadBasket_DMS.csv'
df = pd.read_csv(file)

foods = pd.DataFrame(df.groupby('Item'))
# print(foods)

res = ''
for i in foods[0]:
    print()
    print(i)
    x = input("type : ")
    res += str(i) + ','
    if x == 'f':
        res += 'food\n'
    elif x == 'd':
        res += 'drink\n'
    else:
        res += 'unkown\n'

    # print(res)
print(res)