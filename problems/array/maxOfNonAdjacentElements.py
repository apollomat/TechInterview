
# Given an array of integers, find a maximum sum of non-adjacent elements.
# E.g. [1, 0, 3, 9, 2] should return 10 (1 + 9).
#

def findMax(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    max_val = 0
    for i in range(len(arr))[2:]:
        dp[i] = max(dp[i - 1], arr[i] + dp[i-2])
        max_val = max(dp[i], max_val)

    return max_val


arr = [1, 0, 3, 9, 2]
print findMax(arr)
