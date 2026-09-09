# Pushed: 2026-09-09 15:35:13 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = "([{"
        cl = ")]}"
        for par in s:
            if par in op:
                stack.append(par)
            elif par in cl:
                if not stack:
                    return False
                temp = stack.pop()
                if not ((temp == '(' and par == ")") or (temp == '[' and par == "]") or (temp == '{' and par == "}")):
                    return False

        return not stack