import matplotlib.pyplot as plt

ticker = "KOLabels.csv"
startingAmount = 100

with open(ticker) as f:
    lines = f.read().splitlines()
print('opened file for ticker: ', ticker)

# Start
weeks = []
for line in lines:
    weeks.append(line.split(','))

weeks = weeks[1:]


# weekly
def labelTrading(weekly, money):
    # money = 100
    shares = 0
    position = None

    # Analysis variables
    totalBalance = 0
    grwoth = [money]
    weeks = [i for i in range(len(weekly))]
    minAccount = money
    maxAccount = money
    minWeek = 0
    maxWeek = 0
    prev = 0
    growingDuration = 0
    fallingDuration = 0
    growingMax = 0
    fallingMax = 0

    if weekly[0][-1] == 'Good':
        shares = money / float(weekly[0][2])
        position = 'Hold'

    for i in range(len(weekly) - 1):
        week = weekly[i]
        if weekly[i + 1][-1] == 'Good':
            if position == None:
                shares = money / float(week[2])
                position = 'Hold'
        else:
            if position == 'Hold':
                money = shares * float(week[1])
                position = None

        totalBalance += money
        grwoth.append(money)
        if minAccount != 0 and minAccount > money:
            minAccount = money
            minWeek = i

        if maxAccount > money:
            maxAccount = money
            maxWeek = i

        if money >= prev and position != 'Hold':
            growingDuration += 1
            fallingDuration = 0
            if growingDuration > growingMax:
                growingMax = growingDuration
        else:
            fallingDuration += 1
            growingDuration = 0
            if fallingDuration > fallingMax:
                fallingMax = fallingDuration

    print('Average money owned = ', totalBalance/len(weekly))
    plt.plot(weeks,grwoth)
    print('Max was ', maxAccount, ' At week ', maxWeek, '(expected to be at end because of growth)')
    print('Min was ', minAccount, ' At week ', minWeek, '(expected to be at start because of growth)')

    money += shares * float(weekly[-1][2])
    print('Final Amount(Sold all held shared at end of year) = ', money)

    print('The longest period of growth was ', growingMax)
    print('The longest period of falling values was ', fallingMax)
    plt.show()

    return money


# Question 1
print('\nQuestion 1')
revenue = labelTrading(weeks[:53], money=startingAmount)
print('Total Profit for year 1 with labels = ', revenue - 100)

# Question 2
print('\nQuestion 2')
revenue = labelTrading(weeks[53:], money=startingAmount)
print('Total Profit for year 2 with labels = ', revenue - 100)
