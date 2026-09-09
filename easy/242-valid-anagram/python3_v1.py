# Pushed: 2026-09-09 15:40:34 UTC
# Difficulty: Easy
# Runtime: 15 ms
# Memory: 20.5 MB

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)