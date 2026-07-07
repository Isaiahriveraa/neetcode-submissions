class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # we must take 2 courses
        adj_list = [[] for _ in range(numCourses)]
        # must take course b before we take a meaning b should have the nei of a
        num_preq_needed = [0] * numCourses

        for pre, crs in prerequisites:
            adj_list[crs].append(pre)
            num_preq_needed[pre] += 1
        
        q = deque()

        for i, node in enumerate(num_preq_needed):
            if node == 0:
                q.append(i)
                
        visited = set()

        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            
            for nei in adj_list[node]:
                num_preq_needed[nei] -= 1
                if num_preq_needed[nei] == 0:
                    q.append(nei)
                
        
        return len(visited) == numCourses

