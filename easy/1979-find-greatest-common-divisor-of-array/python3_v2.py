# Pushed: 2026-09-09 15:43:02 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        while b:
            a, b = b, a % b
        return a