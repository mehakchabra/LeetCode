class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_found = True
        while num_found:
            if original in nums:
                original *= 2
            else:
                num_found = False
        return original
        