class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque([0])
        maxQ = deque([0])
        l = 0
        res = 1

        for r in range(1, len(nums)):

            while maxQ and nums[maxQ[-1]] < nums[r]: # while the maxQ end is < nums[r]
                maxQ.pop()
            maxQ.append(r)
            while minQ and nums[minQ[-1]] > nums[r]: # while the maxQ end is < nums[r]
                minQ.pop()
            minQ.append(r)

            while (nums[maxQ[0]]) - (nums[minQ[0]]) > limit:
                l += 1
                while minQ[0] < l: # not in window remove
                    minQ.popleft()
                while maxQ[0] < l: # not in window remove
                    maxQ.popleft()
            res = max(res, r - l + 1)
    
        return res