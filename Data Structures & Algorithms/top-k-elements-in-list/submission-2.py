
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        @problem
        - nums -> List[int]
        - k -> int
    
        @goal return the k most freq elements within in an array

        @return List[int] | any order

        @algos || data structures
        - top K hints the following algos || data structures
            - heap data structure, bucket sorting algo
        
        We have to process nums and keep track of how many times that int appears in the array
        - we can use Counter(nums)
        """
        num_to_freq = Counter(nums) # get the frequency of a number | example: [0, 1] num_to_freq = {0: 1, 1: 1}
        res = [] # returning a List[int]

        buckets = [[] for _ in range(len(nums) + 1)]
        
        # fill the indexs of buckets that correspond to a list of ints that share the same freq 
        # @example [0, 1]
        # [[0, 1], [], [] if k == 2 -> return [0, 1] are the top k elements
        
        # filling the buckets
        for num, freq in num_to_freq.items(): # get the key and the val and the same time using .items()
            buckets[freq].append(num)
        
        # we need to get the most freq elements showing up in array
        # iterate through buckets in reverse that way we can fill up the res with the most freq elements first
        # whenever we hit the length of k we return

        for index in range(len(buckets) - 1, -1, -1):  # iterating thru buckets in rev
            for cur_bucket in buckets[index]:
                res.append(cur_bucket)

                if len(res) == k:
                    return res


        return res

