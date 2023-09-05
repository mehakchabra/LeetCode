class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        lst = []
        zero = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        for i in nums:
            if i !=0:
                lst.append(i)
            else: zero += 1
        return lst+[0]*zero
        