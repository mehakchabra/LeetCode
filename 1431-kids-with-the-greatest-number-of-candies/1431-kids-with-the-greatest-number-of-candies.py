class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = []
        for i in range(0,len(candies)):
            candies[i] += extraCandies
            if(candies[i] == max(candies)):
                greatest.append(True)
            else: greatest.append(False)
            candies[i] -= extraCandies
        return greatest
