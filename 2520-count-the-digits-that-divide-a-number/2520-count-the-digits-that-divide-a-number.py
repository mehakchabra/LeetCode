class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num
        num = list(str(num))
        for i in num:
            if n % int(i) == 0:
                count+=1
        return count
