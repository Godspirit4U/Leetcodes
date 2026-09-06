# Pushed: 2026-09-06 11:16:10 UTC
# Difficulty: Easy
# Runtime: 13 ms
# Memory: 19.3 MB

class Solution:

    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        rank = {
            'I': 7,
            'V': 6,
            'X': 5,
            'L': 4,
            'C': 3,
            'D': 2,
            'M': 1
        }
        result = 0
        i = 0
        while i <= (len(s) - 1):
            if (i < len(s) - 1) and rank[s[i]] > rank[s[i+1]]:
                result += romans[s[i+1]] - romans[s[i]]
                i += 2
            else:
                result += romans[s[i]]
                i += 1
        return result