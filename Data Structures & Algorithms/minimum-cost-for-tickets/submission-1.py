class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        memo = {}
        durations = [1, 7, 30]

        def dfs(i):

            if i == len(days): # we have no days anymore we found an ans
                return 0
            
            if i in memo: # use the cached res, we have already done this subproblems so return the min
                return memo[i]
            
            res = float('inf')

            for pass_index in range(3):

                duration = durations[pass_index] # either 1, 7 or 30 
                j = i # how much days we have processed

                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                
                res = min(res, costs[pass_index] + dfs(j))

            # store in the cache
            memo[i] = res
            
            return res

        return dfs(0)
