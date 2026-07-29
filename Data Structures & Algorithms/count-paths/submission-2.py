class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        answer = [[0] * n for i in range(m)]
        
        answer[0][0] = 1

        for r in range(m):
            for c in range(n):
                
                if r == 0 and c == 0:
                    continue

                left_nei = answer[r][c - 1] if c - 1 >= 0 else 0
                top_nei = answer[r - 1][c] if r - 1 >= 0 else 0
                
                # update the current 
                answer[r][c] = left_nei + top_nei
        
        print(answer)

        return answer[m - 1][n - 1]
