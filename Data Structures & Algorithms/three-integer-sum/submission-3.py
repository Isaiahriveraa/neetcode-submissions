class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(n log n)
        res = []     # List[List[int]]
        for i, n in enumerate(nums):

            if n > 0:
                return res

            if i - 1 >= 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                cur_sum = n + nums[l] + nums[r]

                if cur_sum > 0:
                    r -= 1  # lower sum
                elif cur_sum < 0:
                    l += 1  # raise sum
                elif cur_sum == 0:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1

                    # if our current l ptr is the same as the prev move l
                    # to prevent dupes.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res

                    