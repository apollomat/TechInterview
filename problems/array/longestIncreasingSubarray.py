# Longest increasing subarray
# Given an array containing n numbers.
# #The problem is to find the length of the longest contiguous subarray such that
# every element in the subarray is
# strictly greater than its previous element in the same subarray.
# Time Complexity should be O(n).

def longest(a):
    max = 0
    curr_size = 0
    for indx in range(len(a))[1:]:
        if a[indx] > a[indx - 1]:
            curr_size += 1
        else:
            if curr_size > max:
                max = curr_size

            curr_size = 1
    return max
a = [5, 6, 3, 5, 7, 8, 9, 1, 2] # 5

print longest(a)
b = [12, 13, 1, 5, 4, 7, 8, 10, 10, 11] # 4
print longest(b)
