class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)

        indx = 1
        for pos in range(len(nums))[2:]:
            if nums[indx] == nums[pos] and nums[indx - 1] == nums[pos]:
                continue
            else:
                indx += 1
                nums[indx] = nums[pos]
        return indx + 1
