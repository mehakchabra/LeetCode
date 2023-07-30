class Solution:
    def reverseWords(self, s: str) -> str:
        str1 = s.split()
        str2=[]
        for i in str1:
            str2.append(i[::-1])
        return " ".join(str2)