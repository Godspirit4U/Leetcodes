# Pushed: 2026-10-08 04:13:39 UTC
# Difficulty: Medium
# Runtime: 2 ms
# Memory: 19.6 MB

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        visited = [False] * len(nums)
        def backtrack(current_path):
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    current_path.append(nums[i])
                    
                    backtrack(current_path)
                    
                    current_path.pop()
                    visited[i] = False
                    
        backtrack([])
        return result