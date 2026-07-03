class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # first make an adj List
        adj_list = [[] for _ in range(n + 1)]

        for node, nei, weight in times:
            adj_list[node].append([weight, nei]) # index, (weight, nei)

        visited = set()
        heap = ([(0, k)])
        # initilize the q with the start and the node

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)

            if len(visited) == n:
                return time
            
            for wt, nei in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(heap, (wt + time, nei))
            
        return -1
                






