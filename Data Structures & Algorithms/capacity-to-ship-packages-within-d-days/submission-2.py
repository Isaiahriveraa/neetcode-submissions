class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        res = r

        def canShip(rate):
            
            carry = 0
            time = 1

            for w in weights: # process all weights
            
                if carry + w > rate:
                    carry = 0
                    time += 1
                    
                if time > days:
                    return False

                carry += w

            return True

        while l <= r:
            rate = (l + r) // 2
            
            if canShip(rate):

                res = min(res, rate)
                # try to lower the rate to see if we can get a smaller rate that will allow us to process all the packages within x days
                r = rate - 1
            else: # our time is > days so we need a higher rate
                l = rate + 1
            
        return res
                
            
