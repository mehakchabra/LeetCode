class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse1 = str(num)[::-1]
        reverse1 = int(reverse1)
        reverse2 = str(reverse1)[::-1]
        reverse2 = int(reverse2)
        return num == reverse2
        