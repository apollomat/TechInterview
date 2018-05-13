

def minSize(array, s):
    min_size = 1000
    for indx, value in enumerate(array):
        sum = 0
        for j in range(indx, len(array)):
            sum += array[j]
            if sum == s:
                print "Found between j and indx: " + str(indx) + " " + str(j)
                min_size = min(min_size, j - indx + 1)
                break
    return min_size


def minSubarrayON(arr, s):
    sum = 0
    left = 0
    curr = 0
    min_length = 10000
    while curr < len(arr):
        sum += arr[curr]
        while sum >= s:
            min_length = min(min_length, curr - left + 1)
            sum -= arr[left]
            left += 1
        curr += 1
    return min_length




array = [2,2,1,2,4,3]
s = 7 # return 4,3

# print minSize(array, s)
print minSubarrayON(array,s)
