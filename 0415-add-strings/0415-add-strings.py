import sys
sys.set_int_max_str_digits(10**6)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sum1 = int(num1) + int(num2)
        return str(sum1)
        