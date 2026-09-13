class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # we have to make zip arra
        pos_car =   [(p, s) for p, s in zip(position, speed)]
        pos_car.sort(reverse=True) # reverse the pos_car array that way the tuples are are sorted with the starting pos that are highest because since they are ahead in pos a car cannot pass them
        
        stack = []
        for i in range(len(pos_car)):
            pos, rate = pos_car[i]
            eta = float(target - pos) / (rate) # Target - pos / rate = estimated time of arrival

            # if we have a eta that arrives before the top of the stack we cannot add a car because its already part of the fleet

            if not stack or eta > stack[-1]: # it arrives later meaning its own fleet
                stack.append(eta)
        
        return len(stack)


        
