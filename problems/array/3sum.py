def threeSum(self,nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    result = []
    i = 0
    for i in xrange(len(nums) - 2):
        if(i > 0 and nums[i - 1] == nums[i]):
            continue
        if nums[i] > 0:
            return result
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([nums[left], nums[i], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result




if __name__ == "__main__":
    a = [-1, 0, 1, 2, -1, -4, 5, 5, 5]
#  [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
    end = threeSum(a)
    print a
