# Pushed: 2026-10-05 15:28:39 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        valid_index = 0
        for num in nums:
            if num != val:
                nums[valid_index] = num
                valid_index += 1
        return valid_index