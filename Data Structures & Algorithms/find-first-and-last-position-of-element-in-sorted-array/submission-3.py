class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def search(target):
            l, r = 0, len(nums)

            while l < r:
                m = (l + r) // 2

                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1

            return l

        left = search(target)
        right = search(target + 1)

        return [left, right - 1] if (left < len(nums) and nums[left] == target) else [-1,-1]