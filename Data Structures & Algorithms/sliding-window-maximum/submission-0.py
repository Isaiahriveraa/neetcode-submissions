class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        """
        [1, 2, 1, 0, 4, 2, 6] k = 3

        Goal is to return the list that contains the max elemetn in the window at each step

        I think that we should just store the index of the number 

        the approach here is a monotonic queue

        q can add in o(1) on the right and the left

        if the current number is window otherwise we just remove it
        also we only care ab the number that is the cur max in the window meaning we keep removing the rest if they are smaller than the 

        k = 3
        q = []
        i = 0 
        [1]
        i = 1 
        [(1, 2)] cur = nums[1] = 2
        while nums[q[0] < cur:
            q.popleft() # remove the current max in the subarray that way we can access the new max in constant time
        
        """

        q = deque()
        res = [] # int
        l = 0

        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop() # keep the deque in descending order [3, 2, 1] keeping the max all the way the left of the deque (quick access)
            
            # now append the res 
            q.append(r)
            

            if (r - l + 1) == k: # now we hit our subarray limit now we must append the max
                
                # check if the left is in bounds
                while q[0] < l:
                    q.popleft()
                res.append(nums[q[0]])
                l += 1
            
        return res
                
