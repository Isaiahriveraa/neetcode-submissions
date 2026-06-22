class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        count = Counter(words[0]) # we need one for the sample to check if the rest follow the same amt of these commonChars

        for w in words:
            cur_cnt = Counter(w)
            for c in count:
                count[c] = min(count[c], cur_cnt[c])
        
        res = []
        for c in count:
            for i in range(count[c]):
                res.append(c)
        
        return res