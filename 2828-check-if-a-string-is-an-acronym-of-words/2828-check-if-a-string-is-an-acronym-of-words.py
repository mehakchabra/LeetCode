class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        string = ""
        for w in words:
            string += w[0]
        if string == s: return True
        return False