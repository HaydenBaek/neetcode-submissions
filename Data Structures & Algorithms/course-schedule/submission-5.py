class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        visited = set()

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        
        def dfs(node):

            if node in visited:
                return False
            
            visited.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True