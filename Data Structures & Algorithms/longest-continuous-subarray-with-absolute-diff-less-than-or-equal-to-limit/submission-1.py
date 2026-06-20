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
                if minQ[0] < l: # not in window remove
                    minQ.popleft()
                if maxQ[0] < l: # not in window remove
                    maxQ.popleft()
            # now we have a valid window to check if its good 
            res = max(res, r - l + 1)
    
        return res