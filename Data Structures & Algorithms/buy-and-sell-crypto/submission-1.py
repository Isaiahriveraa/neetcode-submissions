class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        given proices where the each index represents the price of 
        the coin on that particular day

        Im allowed to choose one single day when to buy the coin
        and choose the day when to sell it (future) 

        goal: return the max profit I can achieve

        Algos:
        greedy?

        [10,1,5,6,7,1]
        buy, sell, profit = 10, 1, = -9
        set l = r because we are making no profit
            1 < buy in (l) if r < l:
        buy, sell, profit = 1, 5, 4
        buy, sell, profit = 1, 6, 5
        buy, sell, profit = 1, 7, 6
        buy, sell, profit = 1, 1, 0
        """
        profit = 0
        l, r, n = 0, 1, len(prices) - 1
        while r <= n:
            #if a day is less than the cur buy price make us buy at the
            #current price
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1


        return profit