class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for u, v, price in flights:
            adj[u].append((v, price))
        
        distance = [float('inf')] * n
        distance[src] = 0

        q = deque()
        q.append((src, 0, 0,)) #(start, stops, cost) starting with 0 stop and 0 cost

        while q:
            city, stops, cost = q.popleft()

            if stops > k: continue

            for nei, price in adj[city]:
                new_cost = cost + price

                if new_cost < distance[nei]:
                    distance[nei] = new_cost
                    q.append((nei, stops + 1, new_cost))
        
        return -1 if distance[dst] == float('inf') else distance[dst]