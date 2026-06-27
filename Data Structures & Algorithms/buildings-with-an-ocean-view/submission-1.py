class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        res = [n-1]
        for i in range(n - 2, -1, -1):
            # if the difference is > 0 we have a view
            difference = heights[i] - heights[res[-1]]
            if difference > 0:
                res.append(i)
        
        return res[::-1]

