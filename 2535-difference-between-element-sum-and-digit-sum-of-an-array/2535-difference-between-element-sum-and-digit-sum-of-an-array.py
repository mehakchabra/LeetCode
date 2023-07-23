class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for num in nums:
            sum1 += num
            n=num
            while n>0:
                sum2 = sum2 + n%10
                n = n//10
        return abs(sum1-sum2)
