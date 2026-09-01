class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """
        n cars 

        pos[i]
        speed[i]

        pair them up using zip
        """

        fleet = [(pos, rate) for pos, rate in zip(position, speed)]
        fleet.sort(reverse=True)

        # we want it in reverse because we want the car that has the lead pos to be certain that way we can make sure that if the car tries to pass the one in the front we will consider to part of the fleet rather than just adding it as a seperate fleet
        stack = []

        for pos, rate in fleet:

            # calculation how long it takes to reach the pos
            arrival = (target - pos) / rate

            if not stack or arrival > stack[-1]:
                stack.append(arrival)
        
        return len(stack)
