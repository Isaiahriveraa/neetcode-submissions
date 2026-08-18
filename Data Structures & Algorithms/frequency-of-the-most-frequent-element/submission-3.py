class Solution: 
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        naive approach: O(N^2) -> we keep recalulating the current window sum we can optmize by keeping track of the window

        nums.sort()  # that way we can make sure that we are updating the numbers on the left to try to get them to match the value
        res = 1
        for r in range(len(nums) - 1, -1, -1):  # iterating in reverse
            cur_num = nums[r]
            l = r - 1
            spending = k
            while l >= 0 and spending > 0:
                # try to get the number equal to cur_num
                if nums[r] - nums[l] <= spending:
                    spending -= nums[r] - nums[l]
                    res = max(r - l + 1, res)
                    l -= 1
                else:
                    break
        """
        nums.sort()  # that way we can make sure that we are updating the numbers on the left to try to get them to match the value
        res = window_sum = l = 0
        for r in range(len(nums)):  # iterating in reverse

            window_sum += nums[r]  # add the current number into the window

            while nums[r] * (r - l + 1) > window_sum + k:  # can't afford the allocation of k
                window_sum -= nums[l]
                l += 1

            # we can afford so record the res
            res = max(res, r - l + 1)

        return res

