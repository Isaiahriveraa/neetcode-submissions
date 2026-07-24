class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = [n - 1]
        for i in range(n - 1, -2, -1):
            
            height = heights[i]

            if height > heights[stack[-1]]:
                stack.append(i)
        
        
        return stack[::-1]