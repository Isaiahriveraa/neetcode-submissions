class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """ 
        0 index array
        
        @params
        -   nums -> arr[int]
        -   p number of pairs that we have
            - we are trying to find out whats the min of the max's differences among the p
            - goal is to return the min difference among the p pairs results 
        
        @example

        [10, 1, 2, 7, 1, 3] | p = 2

        @algo
        
        0) check if p == 0: return 0
        1) sort the nums 
        2) figure out if we have p pairs for a number 
            @example    
            - if we have 1 pair with diff is 0 -> return 0
        3) [GREEDY]
        - since its sorted we can use that to our advangtage and the right nei should be the min diff that we can get from the array

        4) if we find a pair that satifies a number (we can't use an index more than once) -> i += 2
            else: 
                i += 1
        5) We can use binary search:
            - given the constraints we can see that the nums[i] range is 1 - 10**9
            - goes back to saying if we can satfiy p pairs for a number we can try to go lower 
            - if we can't satify then we have to go right
            - Lets say M = 10**9
            - log(M)< n^2

        N * P solution  -> we can do DP algo + greedy -> P <= N / 2 -> N * N/2 -> N^2

        arguably N^2

        Meaning that the binary search algo time complexity
        - N log n -> sorting the nums array
        - Validate if there are p pairs for a number -> "threshold"
        - iteration of nums -> N
        - Left bound -> 0 | Right bound -> 10**9 -> M
        - eliminate half of the results each time in the range -> range gets halfed each time meaning (log M)
        - Do that for all numbers in the array -> N log M < N * P <= N^2
        """

        if p == 0:
            return 0
        
        # sort first
        nums.sort() # GREEDY -> Look at nei

        """
        @purpose: 
            - Validate if this threshold can get p pairs 
        @example
            - nums = [4,2,1,2] | p = 1
            - sort nums -> [1, 2, 2, 4]
        """
        L, R = 0, 10**9
        res = float('inf')
        def isValid(threshold):
            # make sure that we only use an index once
            i = cnt = 0 # cnt represents the amount of pairs that satifies the threshold

            while i <= len(nums): # iterating over nums 
                if i + 1 < len(nums) and abs(nums[i] - nums[i + 1]) <= threshold:
                    cnt += 1
                    i += 2 # we used these 2 indexes so we must increment by 2
                else:
                    # we didnt find a pair
                    i += 1 # possible that the next index can find a nei on the right that satfies the <= threshold
                # early return 
                if cnt == p: # we can find p pairs for this threshold 

                    return True

        # binary search
        while L <= R:

            M = L + (R - L) // 2 # prevent int overflow

            if isValid(M):
                # try to get a lower threshold that satfies p pairs
                res = M
                R = M - 1
            else: # we didnt get P pairs so we need to higher the threshold
                L = M + 1
    
        return res

