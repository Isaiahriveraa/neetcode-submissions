class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        res = 0
        heapq.heapify_max(stones)

        while len(stones) > 1:
            y, x = heapq.heappop_max(stones), heapq.heappop_max(stones)
            print(y, x)
            if x < y:
                heapq.heappush_max(stones, y - x)
        
        return stones[0] if stones else res