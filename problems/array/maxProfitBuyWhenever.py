# You are given the stock prices for a set of days .
#Each day, you can either buy one unit of stock, \
#sell any number of stock units you have already bought,
##or do nothing. What is the maximum profit you can obtain
### by planning your trading strategy optimally?**


# Max profit when you can buy and sell whenever
def maxProfit(a):
    profit = 0
    max = a[-1]

    for i in range(len(a) - 2, -1, -1):
        if a[i] > max:
            max = a[i]
        else:
            profit += (max - a[i])

    return profit

a = [31,312,3,35,33,3,44,123,126,2,4,1]
print maxProfit(a)
b = [1,2, 100] # 197    
