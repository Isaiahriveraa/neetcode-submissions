class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(pos, rate) for pos, rate in zip(position, speed)]
        pos_speed.sort(reverse=True)
        
        car_fleets = []
        
        position_first_car, speed = pos_speed[0]
        car_fleets.append((target - float(position_first_car)) / speed)

        for i in range(1, len(pos_speed)):
            pos, rate = pos_speed[i]
            ETA = (target - pos) / rate
            car_ahead = car_fleets[-1]
            if ETA > car_ahead: 
                car_fleets.append(ETA)
        
        return len(car_fleets)
