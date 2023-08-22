class Solution:
    def convertToBase7(self, num: int) -> str:
        n=num
        num1=""
        sign = 0
        if num == 0: return '0'
        if num<0:
            sign = 1
            num = abs(num)
        while num!=0:
            num1 += str(num % 7)
            num //= 7
        if sign == 1: 
            num1+= "-"
        return num1[::-1]

        
