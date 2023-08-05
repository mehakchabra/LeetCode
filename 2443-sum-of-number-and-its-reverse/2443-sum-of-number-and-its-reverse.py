class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        for i in range(num):
            reverse_i = int(str(i)[::-1])
            if reverse_i + i == num:
                return True
        return False