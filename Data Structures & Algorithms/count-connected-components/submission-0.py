class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        #undirected, so add both ways
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        def dfs(i):
            #no new component found
            if i in VISITED:
                return 0
            #if not visited, add it to visited
            VISITED.add(i)

            #recursive call to dfs() all neighbors of the number
            #we are visiting 
            for j in graph[i]:
                dfs(j)
            return 1
        
        VISITED = set()
        
        sum = 0
        for i in range(n):
            sum += dfs(i)

        return sum