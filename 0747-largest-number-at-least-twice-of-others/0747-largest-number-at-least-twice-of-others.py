class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        original = list(nums)
        nums.sort()
        largest = nums[-1]
        index_largest = original.index(largest)
        for i in range(len(nums)-1):
            if 2 * nums[i] <= largest:
                continue
            else:
                return -1
        return index_largest
            
