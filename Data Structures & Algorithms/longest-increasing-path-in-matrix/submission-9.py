class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # given a 2d grid where there is no negative numbers

        # return the length of the longest streak for a path that is increasing
        # I think we care about the prev state of where we came from and how to prevent cycles
        # I can move in 4 directions
        
        n = len(matrix)
        m = len(matrix[0])
        memo = {}

        def dfs(r, c, prev):
            # bounds check
            
            if (r < 0 or r >= n or c < 0 or c >= m or matrix[r][c] <= prev):
                return 0
            
            if (r, c) in memo: # already calculated it
                return memo[(r, c)]
            
            res = 1
            cur = matrix[r][c]
            res = max(res, 1 + dfs(r - 1, c, cur))
            res = max(res, 1 + dfs(r + 1, c, cur))
            res = max(res, 1 + dfs(r, c - 1, cur))
            res = max(res, 1 + dfs(r, c + 1, cur))

            memo[(r, c)] = res

            return res

        for r in range(n):
            for c in range(m):
                dfs(r, c, -1)
        
        return max(memo.values())
                





            