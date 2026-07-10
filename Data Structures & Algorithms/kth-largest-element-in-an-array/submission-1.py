class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for n in nums:

            heap.append(n)
        
        heapq.heapify(heap)
        
        while heap and len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]