class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
# Approach 1: Brute Force (O(n^2))

        # majority = set()

        # for i in nums:
        #     if nums.count(i) > len(nums)//3:
        #         majority.add(i)
        # return list(majority)
    
# Approach 2:  Using HashMap  (O(n))
        # majority = set()
        # cnt = {}
        # for n in nums:
        #     cnt[n] = cnt.get(n,0) + 1
        #     if cnt[n] > len(nums)//3:
        #         majority.add(n)
        # return list(majority)

# Approach 3: Boyer - Moore Algorithm (SC: O(1))
        num1,num2 = -1,-1
        c1,c2 = 0,0
        majority = set()

        for el in nums:
            if el == num1: c1+=1
            elif el == num2: c2+=1
            elif c1==0: 
                num1 = el
                c1 = 1
            elif c2 == 0:
                num2 = el
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        if nums.count(num1) > len(nums)//3: majority.add(num1)
        if nums.count(num2) > len(nums)//3: majority.add(num2)
        return list(majority)
        




            



        