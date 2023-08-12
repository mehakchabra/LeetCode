class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        y=0
        while(num>0):
            y = y*10 + num%10
            num//=10
        return x==y