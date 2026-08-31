class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # returnt he kth largest lemeent in the array we keep 
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
        
        while len(heap) > k:
            heapq.heappop(heap)

        res = heapq.heappop(heap) 

        return res
