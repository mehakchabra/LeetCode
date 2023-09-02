class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        array = []
        for i in arr:
            if arr.count(i) == 1:
                array.append(i)
        if len(array) < k:
            return ""
        return array[k-1]