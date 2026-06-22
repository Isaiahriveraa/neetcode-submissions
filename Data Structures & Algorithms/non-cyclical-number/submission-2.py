class Solution:
    def isHappy(self, n: int) -> bool:
        # turn the n into a str

        seen = set()
        while n != 1:
            res = 0
            for i in str(n):
                res += int(i)**2
            if res == 1:
                return True
            if res in seen:
                return False
            seen.add(res)
            n = res
        
        return n == 1