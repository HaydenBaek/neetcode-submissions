class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        been = set()

        points = [0, 0]

        been.add(tuple(points))

        for c in path:

            if c == "N":
                points[1] += 1
            
            if c == "E":
                points[0] += 1

            if c == "S":
                points[1] -= 1
            
            if c == "W":
                points[0] -= 1
            
            if tuple(points) in been:
                return True
            
            been.add(tuple(points))
        
        return False
