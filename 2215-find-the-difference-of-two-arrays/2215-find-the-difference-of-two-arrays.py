class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answers1 = []
        answers2 = []
        answers = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in answers1:
                answers1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in answers2:
                answers2.append(nums2[i])
        answers.append(answers1)
        answers.append(answers2)
        return answers

