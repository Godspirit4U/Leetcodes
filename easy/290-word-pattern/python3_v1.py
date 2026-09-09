# Pushed: 2026-09-09 15:40:54 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        d = {}
        for i in range(len(words)):
            if pattern[i] not in d:
                if words[i] in d.values():
                    return False
                d[pattern[i]] = words[i]
            elif d[pattern[i]] != words[i]:
                return False
        return True