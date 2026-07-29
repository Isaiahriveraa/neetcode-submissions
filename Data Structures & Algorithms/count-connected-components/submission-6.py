class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        children = [1] * n

        def find(n1):# find the upmost parent
            if n1 != par[n1]:
                par[n1] = find(par[n1])
            
            return par[n1]
        
        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return #already have the same parent
            
            if children[p1] >= children[p2]: # p1 has more children
                children[p1] += children[p2]
                par[p2] = p1
            else: 
                children[p2] += children[p1]
                par[p1] = p2
            
            return
        
        res = 0
        
        for n1, n2 in edges:
           union(n1, n2)

        for i in range(n):
            if par[i] == i:
                res += 1
        
        return res

