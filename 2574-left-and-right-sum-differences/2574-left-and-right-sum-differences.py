class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            left_sum = sum(nums[0:i+1])
            right_sum = sum(nums[i:len(nums)+1])
            answer.append(abs(left_sum-right_sum))
        return answer
        