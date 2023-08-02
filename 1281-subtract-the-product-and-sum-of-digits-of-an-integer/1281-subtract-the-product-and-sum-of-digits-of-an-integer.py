class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1 = 0
        product = 1
        while n>0:
            d = n%10
            sum1 += d
            product *= d
            n //= 10
        return product - sum1