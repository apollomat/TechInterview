

def longestConsecutiveSequence(arr):
    s = set()

    for i in arr:
        s.add(i)
    max_count = 0
    for value in arr:
        right = value + 1
        left = value - 1
        count = 1
        while left in s:
            count += 1
            left -= 1

        while right in s:
            count += 1
            right += 1

        max_count = max(count, max_count)
    return max_count


arr = [100,400,1,57,2,62,3,54,4]
print longestConsecutiveSequence(arr)
# 1 2 3 4
#
