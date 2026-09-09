# Pushed: 2026-09-09 15:39:46 UTC
# Difficulty: Easy
# Runtime: 1148 ms
# Memory: 19.2 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        
        while i * i <= x:
            i = i + 1
        
        return i - 1