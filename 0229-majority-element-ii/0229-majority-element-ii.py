class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Approach 1: Brute Force

        majority = set()

        for i in nums:
            if nums.count(i) > len(nums)//3:
                majority.add(i)
        return list(majority)
            



        