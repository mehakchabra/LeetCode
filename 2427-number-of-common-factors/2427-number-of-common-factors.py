class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        minimum = min(a,b)
        factor = 0
        for m in range(1, minimum+1):
            if a % m == 0 and b % m == 0:
                factor += 1
        return factor
        