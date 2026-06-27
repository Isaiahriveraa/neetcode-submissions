class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i, j = 0, 0 
        res = []
        while i < len(firstList) and j < len(secondList):
            f_end, s_end = firstList[i][1], secondList[j][1]
            f_start, s_start = firstList[i][0], secondList[j][0]
            
            end = min(f_end, s_end)
            start = max(f_start, s_start)
            # find the start and the end
            # and increment one of them
            # 0, 2
            # 1, 5 max start is 1 and the min start is 2 so we add
            print(f"{i}, {j} start {start} end {end}")
            if start <= end: # valid intersection
                res.append([start, end])
                if end == f_end:
                    i += 1
                else:
                    j += 1
            elif end == f_end:
                i += 1
            else:
                j += 1
                # place the start 
        return res            