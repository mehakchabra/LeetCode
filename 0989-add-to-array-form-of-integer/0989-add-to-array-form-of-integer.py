import sys
sys.set_int_max_str_digits(10**6)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        string = ''
        for i in num:
            string += str(i)
        sum1 = int(string) + k
        return [int(i) for i in list(str(sum1))]
        
        