class Solution:
    def removePalindromeSub(self, s: str) -> int:
        count=0
        if s==s[::-1]:
            count+=1
        else:
            count+=2
        return count
        