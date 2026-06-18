class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while r > l:
            area = min(heights[r], heights[l]) * (r - l)
            res = max(area, res)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return res
