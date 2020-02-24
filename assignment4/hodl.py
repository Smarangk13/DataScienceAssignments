ticker = "KOLabels.csv"

with open(ticker) as f:
    lines = f.read().splitlines()
print('opened file for ticker: ', ticker)

# Start
weeks = []
for line in lines:
    weeks.append(line.split(','))

weeks = weeks[1:]

# buy and hodl
def yearProfit(opening,closing):
    opening = float(opening)
    closing = float(closing)
    sharesOwned = 100 / opening
    revenue = sharesOwned * closing
    buyHoldProfit = 100 - revenue
    return buyHoldProfit

yearOpen = weeks[0][1]
yearClose = weeks[52][2]
profit = yearProfit(yearOpen, yearClose)
print('Buy and hold profit for year 1 =',profit)

yearOpen = weeks[53][1]
yearClose = weeks[-1][2]
profit = yearProfit(yearOpen, yearClose)
print('Buy and hold profit for year 2 =',profit)

# weekly
def labels(weekly,money):
    # money = 100
    shares = 0
    for week in weekly:
        if week[-1] == 'Good':
            shares = money/float(week[1])
            money = shares*float(week[2])

    return money

revenue = labels(weeks[:53],money=100)
print('Total Profit for year 1with labels = ', revenue-100)
revenue = labels(weeks[53:],money=100)
print('Total Profit for year 2 with labels = ', revenue-100)