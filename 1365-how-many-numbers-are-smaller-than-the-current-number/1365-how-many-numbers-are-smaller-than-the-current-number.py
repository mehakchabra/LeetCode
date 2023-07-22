class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        arr = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i!=j and nums[j] <nums[i]:
                    count+=1
            arr.append(count)
            count = 0
        return arr
