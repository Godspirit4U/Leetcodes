# Pushed: 2026-09-09 15:35:37 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        return [word for word, count in word_counts.items() if count == 1]
