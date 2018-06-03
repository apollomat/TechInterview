class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        dict_of_lengths = defaultdict(list, [])
        longest = 1
        for index in range(len(nums)):
            for j in range(index, len(nums)):
                if nums[j] > nums[index]:
                    dp[j] = max(dp[index] + 1, dp[j])
                    longest = max(longest, dp[j])
        return longest

        
