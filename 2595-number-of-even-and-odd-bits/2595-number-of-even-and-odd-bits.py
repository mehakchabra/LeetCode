class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0 
        odd = 0
        binary = (bin(n)[2:])[::-1]
        for i,v in enumerate(binary):
            if i%2 == 0 and v == "1": even += 1
            if i%2 != 0 and v == "1": odd += 1
        return [even, odd]

        