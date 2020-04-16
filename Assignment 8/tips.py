import pandas as pd

tipFile = 'tips.csv'
df = pd.read_csv(tipFile)

def tipPct(dfx):
    bill = dfx['total_bill'].mean()
    tip = dfx['tip'].mean()
    tipPct = '{0:.2f}'.format((tip/bill)*100)

    return tipPct

# Question 1
print('Question 1')
lunchdf = df[df['time'] == 'Lunch']
dinnerdf = df[df['time'] == 'Dinner']

lunchTipPct = tipPct(lunchdf)
dinnerTipPct = tipPct(dinnerdf)

print('Lunch tip % =',lunchTipPct,'%')
print('Dinner tip % =',dinnerTipPct,'%')

# Question 2
print('\nQuestion 2')
days = df['day'].unique()
print(list(days))

for day in days:
    daydf = df[df['day']==day]
    dayTip = tipPct(daydf)
    print('Tip % on',day,'is =',dayTip,'%')

# Question 3
print('\nQuestion 3')
maxDay = ''
maxTime = ''
maxTip = 0

for day in days:
    daydf = df[df['day'] == day]
    lunchdf = daydf[daydf['time'] == 'Lunch']
    dinnerdf = daydf[daydf['time'] == 'Dinner']
    lunchTip = tipPct(lunchdf)
    dinnerTip = tipPct(dinnerdf)
    if float(lunchTip) > maxTip:
        maxTip = float(lunchTip)
        maxTime = 'lunch'
        maxDay = day

    if float(dinnerTip) > maxTip:
        maxTip = float(dinnerTip)
        maxTime = 'dinner'
        maxDay = day

print('The best day for tips is', maxDay, 'during', maxTime, 'with', maxTip, '%')

# Question 4
print('\nQuestion 4')
correlation = df['total_bill'].corr(df['tip'])
print('The correlation of bill with tip is',correlation)

# Question 5
print('\nQuestion 5')
sizeCo = df['size'].corr(df['tip'])
print('The correlation of size of group with tip is',sizeCo)
if abs(sizeCo) < 0.4:
    print('There is not much correlation between Size of group and tip')
elif sizeCo > 0:
    print('Since the correlation is positive there is a positive influnce of the group size')
else:
    print('Larger groups give smaller tips')

# Question 6
print('\nQuestion 6')
smokerdf = df[df['smoker']=='Yes']
pctSmoker = len(smokerdf)/len(df) * 100
print('The % of smokers is',pctSmoker)

# Question 7
print('\nQuestion 7')
last = 0
res = 'Yes'
for day in days:
    daydf = df[df['day'] == day]
    lunchdf = daydf[daydf['time'] == 'Lunch']
    dinnerdf = daydf[daydf['time'] == 'Dinner']
    lunchTip = tipPct(lunchdf)
    dinnerTip = tipPct(dinnerdf)

    if float(lunchTip) > last:
        last = float(lunchTip)
    else:
        res = 'No'
        break

    if float(dinnerTip) > last:
        last = float(dinnerTip)
    else:
        res = 'No'
        break

print('Does tip increase with time? ', res)

# Question 8
print('\nQuestion 8')

nonSmokerDf = df[df['smoker']=='No']
smokeCo = df['total_bill'].corr(df['tip'])
noSmokeCo = df['total_bill'].corr(df['tip'])

if smokeCo > noSmokeCo:
    print('Smokers tip higher than non smokers')

else:
    print('Non Smokers tip higher than smokers')