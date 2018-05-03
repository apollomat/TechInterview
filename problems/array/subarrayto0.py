def findSubArray(arr):
    sum = 0
    dict_t = {}
    for i in xrange(len(arr)):
        sum += arr[i]

        if sum in dict_t or sum == 0:
            return True
        else:
            dict_t[sum] = i

# Given an array of integers find whether there is a sub-sequence that sums to 0 and return it.
# E.g. [1, 2, -3, 1] => [1, 2, -3] or [2, -3, 1].
arr = [1, 2, -3, 1] #=> [1, 2, -3] or [2, -3, 1].
print findSubArray(arr)
