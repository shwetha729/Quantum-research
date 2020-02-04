

def stringFormattedWeeklyPrices(dailyPrice):
    # n is the length of the items in array
    n = len(dailyPrice)
    x = range(dailyPrice[0], dailyPrice[n-1])
    for i in x:
        lastvalue = range(i, i+7)
        the_average = sum(lastvalue) / 7
        string = str(the_average)
        print(round(the_average, 2))


n = [1, 2, 2, 2, 2, 2, 3, 3, 4, 3, 4, 3, 3, 3, 3]
stringFormattedWeeklyPrices(n)
