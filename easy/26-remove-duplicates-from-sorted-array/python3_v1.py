# Pushed: 2026-09-09 15:37:32 UTC
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 20.5 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for num in nums:
            if k == 0 or num != nums[k-1]:
                nums[k] = num
                k += 1
        return k