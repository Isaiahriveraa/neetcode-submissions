from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_count, col_count = len(grid), len(grid[0])
        mins = 0
        fresh = 0

        # count how many fresh fruits before hand that way we can handle the edge case if there are remaining fresh fruits
        
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == 1: # if its fresh mark ti
                    fresh += 1
                elif grid[r][c] == 2: # if is rotten that means that we must add it to the queue
                    queue.append((r, c))
                # otherwise its 0

        while queue and fresh > 0: # BFS
            
            for i in range(len(queue)):
                current_row, current_col = queue.popleft()
                
                # looking at the nei
                for row_increment, col_increment in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    neighbor_row = current_row + row_increment
                    neighbor_col = current_col + col_increment
                    in_range = 0 <= neighbor_row < row_count and 0 <= neighbor_col < col_count
                    if in_range and grid[neighbor_row][neighbor_col] == 1: # if its in range and the fruit is fresh
                            grid[neighbor_row][neighbor_col] = 2 # mark it as rotten
                            fresh -= 1
                            queue.append((neighbor_row, neighbor_col))
            mins += 1
        return mins if fresh == 0 else -1