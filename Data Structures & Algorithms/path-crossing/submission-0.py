class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        # Given a str where the ith in path  = NSEW
        # start at 0, 9
        # return True if the path crosses it self at any point if i am on location i have previouly visited

        x = y = 0

        visited = set()
        visited.add((0, 0))

        for letter in path:

            if letter == "N":
                y += 1
            elif letter == "S":
                y -= 1
            elif letter == "E":
                x += 1
            else:
                x -= 1
            pos = (x, y)
            if pos in visited:
                return True
            visited.add(pos)

        return False
            