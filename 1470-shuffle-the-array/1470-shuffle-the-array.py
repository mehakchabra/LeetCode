class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        j=0
        for i in range(0,n):
            if j%2==0:
                arr.append(nums[i])
                j+=1
            if j%2 != 0:
                arr.append(nums[i+n])
                j+=1
        return arr

