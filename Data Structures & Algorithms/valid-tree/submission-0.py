class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 > len(edges):
            return False
        # Trees must have n - 1 edges to be a complete tree
        par = [i for i in range(n)]
        children = [1] * n

        def find(n1):
            # find the parent node for this node 
            if n1 != par[n1]: # we must travel higher to the upmost parent
                par[n1] = find(par[n1])
            return par[n1] # return the parent of the n1

        def union(n1, n2):

            # get the parents
            p1, p2 = find(n1), find(n2)

            if p1 == p2: # we have a  cycle so invalid tree
                return False

            # compare the children
            if children[p1] >= children[p2]:
                # add the children to the p1 since it has more children
                # make the par[p2] point to p1
                children[p1] += children[p2]
                par[p2] = p1
            else:
                children[p2] += children[p1]
                par[p1] = p2
            
            return True
        
        for node, edge in edges:
            if not union(node, edge):
                return False
        
        return True
        
             