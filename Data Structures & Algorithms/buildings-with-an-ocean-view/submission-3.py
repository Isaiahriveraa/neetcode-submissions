class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        q = deque([n-1])
        stack = [heights[n - 1]]
        for i in range(n - 1, -1, -1):
            
            height = heights[i]

            if height > stack[-1]:
                stack.append(height)
                q.appendleft(i)
        
        
        return list(q)