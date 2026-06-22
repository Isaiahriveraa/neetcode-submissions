class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        # sorted he can only finish one at a time q?
        # the order they were given
        # arrival and time

        t = total = 0
        for arrival, order in customers:
            t = max(t, arrival) + order
            total += t - arrival
        
        return float(total) / len(customers)