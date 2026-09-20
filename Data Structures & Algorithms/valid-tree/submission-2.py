class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #trees dont have cycle
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        #detecting cycle
        if not dfs(0, -1):
            return False
        
        return len(visited) == n