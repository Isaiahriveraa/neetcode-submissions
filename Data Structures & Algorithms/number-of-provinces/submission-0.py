class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        """
        if ith city and jth city are dir connected:
            its 1
        else: 
            its 0
    
        given n by n
        """
        n = len(isConnected)
        par = [i for i in range(len(isConnected))]
        children = [1] * n

        def find(n):
            
            #find the upmost parent
            if par[n] != n:

                par[n] = find(par[n])

            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return
            
            if children[p1] >= children[p2]:
                children[p1] += children[p2]
                par[p2] = p1
            else:
                children[p2] += children[p1]
                par[p1] = p2


        for i in range(len(isConnected)):
            for j in range(len(isConnected)): 
                if isConnected[i][j] == 1:
                    union(i, j)
                    # i is the row, j is the col

        res = 0

        for i, parent in enumerate(par):
            if parent == i:
                res += 1
            
        return res
        
