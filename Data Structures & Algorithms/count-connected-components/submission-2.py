class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]  
        children = [1] * (n)
    
        def find(n1):

            if n1 != par[n1]:
                par[n1] = find(par[n1])

            return par[n1]      

        def union(n1, n2):

            # find out if they already have the same parent

            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return
            
            # if not then we have to compare the amt of children
            if children[p1] >= children[p2]:
                # add the children to the p2
                # and change the parent
                children[p1] += children[p2]
                par[p2] = p1
            else:
                children[p2] += children[p1]
                par[p1] = p2

            return

        for node, edge in edges:
            union(node, edge)
        
        number_of_comps = 0

        for i, node in enumerate(par):
            if i == node:
                number_of_comps += 1
        
        return number_of_comps