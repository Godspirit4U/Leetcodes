# Pushed: 2026-10-06 16:34:39 UTC
# Difficulty: Easy
# Runtime: 1 ms
# Memory: 21 MB

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result