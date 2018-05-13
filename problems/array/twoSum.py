
def twoSum(arr, target):

    dict = {}
    for indx, value in enumerate(arr):
        if target - value in dict:
            return dict[target-value], indx
        dict[value] = indx

    return -1, -1

values = [2,7,11,15]
target = 17

def twoSumSorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            return left, right

print twoSum(values,target)
print twoSumSorted(values, target)
