class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        num_freq = Counter(nums)

        index_freq = [[] for _ in range(n + 1)]

        for num, occurances in num_freq.items():
            index_freq[occurances].append(num)
    
        res = []
        for i in range(len(index_freq) - 1, -1, -1):
            for n in index_freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res