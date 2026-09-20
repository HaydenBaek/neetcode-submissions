class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        
        E = len(edges)

        if n != E + 1:
            return False
        
        adjacent_list = collections.defaultdict(list)

        for u, v in edges:
            adjacent_list[u].append(v)
            adjacent_list[v].append(u)
        
        visited = [False] * n

        q = deque()
        q.append(0)
        visited[0] = True

        while q:

            current = q.popleft()

            for v in adjacent_list[current]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        return all(visited)
