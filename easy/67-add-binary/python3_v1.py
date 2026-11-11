# Pushed: 2026-11-11 15:14:16 UTC
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 19.3 MB

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = 0
        num2 = 0
        for i, char in enumerate(a[::-1]):
            if char == '1':
                num1 += 2 ** i  
        for i, char in enumerate(b[::-1]):
            if char == '1':
                num1 += 2 ** i  
        result = num1 + num2
        if result == 0:
            return "0"

        binary = ''
        while result > 0:
            binary = str(result % 2) + binary
            result //= 2
        return binary
