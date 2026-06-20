class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # RRDDD
        # -> Radiant

        # goal is try to win

        # 1) have 2 queues
        # 2) insert each letter by idx
        N = len(senate)
        # setup the q's based on index
        R = deque([i for i, c in enumerate(senate) if c == 'R'])
        D = deque([i for i, c in enumerate(senate) if c == 'D'])
    
        while R and D:
            cur = None

            if R[0] < D[0]: # R's turn
                cur = R.popleft()
                R.append(cur + N)
                D.popleft()
            else:
                cur = D.popleft()
                D.append(cur + N)
                R.popleft()

        return "Radiant" if R else "Dire"