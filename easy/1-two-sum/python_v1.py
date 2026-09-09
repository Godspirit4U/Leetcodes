# Pushed: 2026-09-09 15:44:18 UTC
# Difficulty: Easy
# Runtime: 5210 ms
# Memory: 13.4 MB

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i and nums[j] + nums[i] == target:
                        return [i,j]
