class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] > prices[r]:
                # we need to reset
                l += 1
                r = l + 1
            else:
                res = max(prices[r] - prices[l], res)
                r += 1

        return res

