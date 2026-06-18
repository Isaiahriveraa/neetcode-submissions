class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        top k means i can use heap, bucket sorting algorthim?

        given an arr, k, 
        goal reutrn k most freq elements in the array

        [1: 1
        2: 2
        3: 3]
        k = 2 

        return [3,2]

        1) make a freq map
        2) we can use a 2d array that each index means the freq
        3) then we add the number at that index if it was that times freq

        [[][1][2][3]]
        """

        n = len(nums)
        # map = (freq, list(numbers))
        freq_map = Counter(nums)
        idx_freq = [[] for _ in range(n + 1)]

        for n, count in freq_map.items():
            idx_freq[count].append(n)

        res = []

        print(idx_freq)
        for i in range(len(idx_freq) - 1, 0, -1):
            for num in idx_freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return []
                







