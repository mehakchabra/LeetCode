class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        columns = ['a','b','c','d','e','f','g','h']
        coordinates = list(coordinates)
        if (columns.index(coordinates[0]) % 2 == 0 and int(coordinates[1]) % 2 == 0) or (columns.index(coordinates[0]) % 2 != 0 and int(coordinates[1]) % 2 != 0): return True