class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        The numbers were rotated 1-n

        We have a target number that we are looking for 
        Assending order

        algo's:
        Binary search because target, acending (sorted)

        With this problem what we have to do is find which side is sorted:

        [3,4,5,6,1,2]
        the left is sorted and the left > target or the middle >
        """
        n = len(nums)
        l, r = 0, n - 1

        while l <= r: # we are searching for a target so l<=r is more appropriate 
            m = (l + r) // 2
            #if the left number is < middle then the left is acending
            if nums[m] == target:
                return m
            print(nums[m])
            if nums[l] <= nums[m]: # left side is acending
                #if our middle is < than what we need go right because that means the rest of 
                #left is less as well
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else: # the right is sorted 
            # find reasons why target isnt in the right
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
            # if the left is sorted:
                # whata are the reasons not to go here?
                # the middle < target so that means target is on the right
                # the left > target
            # if the right is sorted:
                #if the right is > target target must be on the lef
        return -1#if target not present 