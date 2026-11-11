# Pushed: 2026-11-11 14:47:27 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def sortSentence(self, s: str) -> str:
        result = []
        words = s.split()
        for word in words:
            result.append(word[::-1])
        result.sort()
        result = ' '.join(word[:0:-1] for word in result)
        return result