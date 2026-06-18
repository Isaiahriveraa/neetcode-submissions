class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """

        We need to keep track 
        goal is to return the len of the longest conseq secq of E's that can be formed
        the seq must be 1 greater than the prev
        The elements do not have to be contigious in the original array
        Algo must be O(n)
        seen = 2
        seen = 20

        """
        if not nums: return 0
        res = 0
        mp = defaultdict(int)

        for n in nums: 
            if not mp[n]:
                mp[n] = mp[n - 1] + mp[n + 1] + 1
                mp[n - mp[n - 1]] = mp[n]
                mp[n + mp[n + 1]] = mp[n]
                res = max(res, mp[n])
        return res
                        

            
