def find_max_subarray(arr):
    min_sum = 0
    max_sum = 0
    dp = [0] * len(arr)
    for i, value in enumerate((arr)):
        dp[i] = max(dp[i - 1] + value, value)
        if dp[i] > max_sum:
            max_sum = dp[i]

    return max_sum


arr = [904,40,523,12,-335,-385,-124,481,-31]
print find_max_subarray(arr)
