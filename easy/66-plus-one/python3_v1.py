# Pushed: 2026-09-09 15:39:05 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(d) for d in str(int("".join(map(str, digits))) + 1)]