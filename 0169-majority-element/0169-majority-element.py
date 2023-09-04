class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer - moore algorithm
        res, count = 0,0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res




        # count = {}
        # res, maxCount = 0,0

        # for n in nums:
        #     count[n] = count.get(n,0) + 1
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(count[n], maxCount)
        # return res
                
        
        