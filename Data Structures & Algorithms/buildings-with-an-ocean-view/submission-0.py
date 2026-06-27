class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        res = [n-1]
        tallest_building = heights[n-1]
        for i in range(n - 2, -1, -1):
            # if the difference is > 0 we have a view
            difference = heights[i] - tallest_building
            if difference > 0:
                res.append(i)
            tallest_building = max(tallest_building, heights[i])
        
        return res[::-1]

