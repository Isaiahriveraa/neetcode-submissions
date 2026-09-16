class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        """
        2D array
        heights[r][c] = ht of the cell
        goal is the bottom right
        We can move all ways

        
        1, 1, 2, 4, 4
        abs(2 - 4) = 2
        
        Input: heights = 

        [[1,1,1],
         [3,2,4],
         [2,5,4]]

        Output: 2

        @algo
            - Find the smallest nei 
            - record the largest nei seen
            - traverse 
            - carry it to the bottom right
        """
        start_edge_case = 0
        heap = [(0, 0, 0)] 
        visited = set()  # prevent cycles

        while heap:

            max_cost_so_far, r, c = heapq.heappop(heap)

            if (r, c) in visited: # we have been here before
                continue
            
            visited.add((r, c))

            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                # we are at the bottom right
                return max_cost_so_far

            # look at all nei
            nei = [[0,1],[-1,0], [1,0], [0,-1]] # right, up, down, left

            for dr, dc in nei:
                nr, nc = r + dr, c + dc

                if (0 <= nr < len(heights) and # if element is in bounds
                    0 <= nc < len(heights[0])):

                    new_cost = abs(heights[r][c] - heights[nr][nc]) # new cost it takes to get to nei cell
                    heapq.heappush(heap, (max(max_cost_so_far, new_cost), nr, nc))
       
        return start_edge_case