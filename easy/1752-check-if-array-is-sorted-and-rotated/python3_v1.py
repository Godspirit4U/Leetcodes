# Pushed: 2026-09-09 15:42:14 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):

            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1
