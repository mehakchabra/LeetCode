class Solution:
    def isPathCrossing(self, path: str) -> bool:
        (r, c) = (0, 0)
        coordinates = {(0,0)}
        for i in path:
            if i == 'N': c += 1
            elif i == 'E': r += 1
            elif i == 'S': c -= 1
            else: r -= 1
            if (r, c) in coordinates: return True
            coordinates.add((r, c))
        return False