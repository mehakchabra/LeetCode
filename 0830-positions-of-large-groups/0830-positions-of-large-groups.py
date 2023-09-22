class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []

        l = 0
        while l < len(s):
            r = l + 1

            while r < len(s):
                if s[r] != s[r-1]:
                        break
                r += 1
            
            if r-l >= 3:
                res.append([l,r-1])
            l = r

        return res