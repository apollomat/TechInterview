# find largest continuous sum
def largestSum(a):
    largest = 0
    dp = [0] * (len(a) + 1)

    for i in range(len(a)):
        dp[i] = max(dp[i-1] + a[i], a[i]) # see if you want to include
        if dp[i] > largest:
            largest = dp[i]
    return largest
a = [5, -6, 1, 3, 4, -2, 3, 4, -1]
print largestSum(a) #13
