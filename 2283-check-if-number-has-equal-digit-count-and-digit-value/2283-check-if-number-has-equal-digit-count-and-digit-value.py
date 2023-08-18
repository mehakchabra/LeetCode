class Solution:
    def digitCount(self, num: str) -> bool:
        arr = []
        for i in range(len(num)):
            counter = num.count(str(i))
            if counter == int(num[i]): arr.append(1)
            else: arr.append(0)
        if 0 in arr: return False
        else: return True

        