# Pushed: 2026-09-06 11:17:56 UTC
# Difficulty: Easy
# Runtime: 11 ms
# Memory: 19.4 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        org_num = x
        new_num = 0

        while x > 0:
            digit = x % 10
            new_num = new_num * 10 + digit
            x //= 10

        return new_num == org_num