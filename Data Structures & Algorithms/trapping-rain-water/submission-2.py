class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Every index represents a height of a bar, width of 1

        Thinking of 2 pointers because it helps maximaize the area
        
        Unknown:
        - How can I calculate area of water because there is water that isnt trapped between bars

        if conditions:

            if maxL < maxR:
                move the left ptr if new maxL
                update the maxL
                res ++ maxL - curL
            else:
                move right ptr
                update maxr if new maxR
                res += maxR - cur r

        Approach:
        maxL
        maxR
        l, r = 0, len(height) - 1

        res += min(maxL, maxR)?

        height = [0, 2, 0, 3, 1, 0, 1 ,3, 2, 1]

        maxL, maxR = 0, 1
        the min of the 2 is 0
        update the move the maxL and try to update it and

        maxL - height[l] = 2 - 2 = 0, res += 0 which is true
        l = 1
        move the min(maxL, maxR) -> move right pointer
        r = 9 -> 2 -2 = 0, res += 0
        
        move any of the pointers but by default if they are they are the same height move right

        r = 8
        update maxR = 3 - 3 = 0 res = 0
        min(3, 2) -> move left ptr
        l += 1 -> l = 3
        2 - 0 = 2, res = 2, l = 3, r = 8, maxL = 2, maxR = 3
        move maxL
        3 - 3 = 0, res = 2, l = 4, r = 8, maxL = 3, maxR = 3
        move maxL
        3 - 1 = 2, res = 4, l = 5, r = 8, maxL = 3, maxR = 3
        move maxL
        3 - 0 = 3, res = 7, l = 6, r = 8, maxL = 3, maxR = 3
        move maxL
        3 - 1 = 2, res = 9, l = 7, r = 8, maxL = 3, maxR = 3
        move maxL
        3 - 3 = 0, res = 9, l = 8, r = 8, maxL = 3, maxR = 3
        res = 9
        '''
        l, r = 0, len(height) - 1
        maxR = height[r]
        maxL = height[l]
        res = 0
        while l < r:
            if maxL < maxR:
                #move the left ptr
                l += 1
                maxL = max(maxL, height[l])
                res += (maxL - height[l])
            else:
                #move the right ptr
                r -= 1
                maxR = max(maxR, height[r])
                res += (maxR - height[r])
        return res