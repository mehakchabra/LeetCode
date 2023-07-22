class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        arr = []
        for i in range(0,len(nums)):
            sum+=nums[i]
            arr.append(sum)
        return arr
