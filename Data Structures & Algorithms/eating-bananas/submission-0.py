class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        """
        Given piles

        given h which means the number hours we have to complete the piles

        I have to return the min rate that will pass <= h
        """
        l,r = 1, max(piles) # 1 that way we can always eat a banana, max(piles) because we always want to gurantee piles.length <= h meaning that in the worst case we will eat all the bananas with the max rate

        res = r
        while l <= r:

            rate = (l + r) // 2 # mid
            time = 0

            for p in piles:

                time += math.ceil(float(p) / rate) # we want to do ceil that way we can always finish the pile before moving on

            if time <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        
        return res



                

