class Solution:
    def greatestLetter(self, s: str) -> str:
        string = ""
        for i in s:
            if i.isupper() and i.lower() in s:
                string += i
        if len(string) == 0: return ""
        else: 
            lst = list(string)
            return max(lst)
