class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Given the times [ui, vi, ti] ui = source, vi = target node, ti = weight
        #return the min time thar we need to visit all nodes so essentially we can do this with union
        #find 
        #k is the start node 
        # 1 -> 2 -> 3 -> 4 because 1 is already in the cycle meaning taht we found the cheapest and it cost 3 because the inital is free
        res = 0
        adj_list = defaultdict(list)
        for src, node, wt in times:
            adj_list[src].append((wt, node)) #that way we can heap pop it,  node meaning thats where we can travel to if we accepted this weight
        
        # now we have the adj_list set up that means that we need to add the starting node
        min_heap = [(0, k)]
        visited = set()
        while min_heap:
            dist, cur = heapq.heappop(min_heap)
            if cur in visited:
                continue
            visited.add(cur)
            res = max(res, dist)
            # using our cur node explore the neigh
            for wt, nei in adj_list[cur]:
                if nei not in visited:
                    heapq.heappush(min_heap, (dist + wt, nei))
        
        return res if len(visited) == n else -1