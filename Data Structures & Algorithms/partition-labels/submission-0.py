class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {} # store the last index we seen this char

        for i, c in enumerate(s):
            last_seen[c] = i
        
        start = end = 0
        res = []

        for i, c in enumerate(s):
            end = max(last_seen[c], end)

            if i == end: # Reached the end of the cur partition
                res.append(end - start + 1)
                start = i + 1 # Start a new partition
        
        return res