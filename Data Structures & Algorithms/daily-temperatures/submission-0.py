class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        """

        """
        res = [0] * len(temps) 
        stack = [] # (element, idx)
        # days i - idx
        for i, n in enumerate(temps):
            while stack and stack[-1][0] < n:
                element, idx = stack.pop()
                res[idx] = i - idx # days it took to find a warmer day for this index = element
            stack.append((n, i))
        
        return res