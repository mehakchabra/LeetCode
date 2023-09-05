class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0 
        odd = 0
        binary = (bin(n)[2:])[::-1]
        for i,v in enumerate(binary):
            if v == "1" and i%2 == 0: even += 1
            if v == "1" and i%2 != 0: odd += 1
        return [even, odd]

        