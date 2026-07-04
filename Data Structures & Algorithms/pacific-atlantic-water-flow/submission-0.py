class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = set()
        atl = set()

        # trying to find elements that fall into pac and atl sets

        # left row (pac)
        for r in range(len(heights)):
            self.traversal(r, 0, heights, pac)

        for c in range(len(heights[0])):
            self.traversal(0, c, heights, pac)

        for r in range(len(heights)):
            self.traversal(r, len(heights[0]) - 1, heights, atl)

        for c in range(len(heights[0])):
            self.traversal(len(heights) - 1, c, heights, atl)
        
        res = []

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res

    
    def traversal(self, r, c, heights, ocean):
        # already visited this
        if (r, c) in ocean:
            return
        
        ocean.add((r, c))
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (0 <= nr < len(heights) and
                0 <= nc < len(heights[0]) and
                heights[nr][nc] >= heights[r][c]
            ):
                self.traversal(nr, nc, heights, ocean)



