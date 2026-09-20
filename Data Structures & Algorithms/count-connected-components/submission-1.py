class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        sum = 0
        visited = set()

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)
            return 1
        
        for i in range(n):
            sum += dfs(i)
        
        return sum
