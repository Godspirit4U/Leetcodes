# Pushed: 2026-09-09 15:36:05 UTC
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 19.7 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for ch in s.lower():
            if ch.isalnum():
                s1 += ch
        return s1 == s1[::-1]