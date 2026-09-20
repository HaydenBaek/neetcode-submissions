class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        result = []
        path = set()
        done = set()

        def dfs(node):
            if node in path:
                return False
            if node in done:
                return True
            
            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            done.add(node)
            result.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        result.reverse()
        return result