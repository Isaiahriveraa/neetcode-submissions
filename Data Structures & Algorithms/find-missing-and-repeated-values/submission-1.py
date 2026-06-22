class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        res = []
        n = len(grid)
        seen = set()
        for group in grid:
            for n in group:
                if n in seen:
                    res.append(n)
                seen.add(n)
        
        for i in range(1, (n ** n) + 1):
            if i not in seen:
                res.append(i)
                break

        return res

