class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # The main part of this problem is understanding that you want to use the
        # min and the max math operations to your advantage to calculate end is
        # equal to the minimum of the two intervals start is equal to the max 
        #start of the two intervals and then what we have to do is if the start 
        #is less than or equal to the end, then we can add this intersection to 
        #the result. If the end is equal to the first end, we must move the first
        # pointer which correlates to i. Otherwise, the end is equal to the 
        #second end array meaning we have to move j pointer up one otherwise 
        #there's the case where the star is greater than the end, meaning we 
        #have to find which end is causing this, right? So we say if end is 
        #equal to the first end, we must increment i that way we can have a 
        #valid intersection chance. Otherwise the end is equal to the second 
        #end array meaning we have to increment j.
        # The time complexity is O of M + N
        
        i, j = 0, 0 
        res = []
        while i < len(firstList) and j < len(secondList):
            f_end, s_end = firstList[i][1], secondList[j][1]
            f_start, s_start = firstList[i][0], secondList[j][0]
            
            end = min(f_end, s_end)
            start = max(f_start, s_start)
            if start <= end: # valid intersection
                res.append([start, end])
                
            if end == f_end:
                i += 1
            else:
                j += 1
        return res            