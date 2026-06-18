from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        res = defaultdict(list)
        for word in strs:
            cur = [0] * 26
            for char in word:
                cur[ord('a') - ord(char)] += 1
            res[tuple(cur)].append(word)

        return list(res.values()) 