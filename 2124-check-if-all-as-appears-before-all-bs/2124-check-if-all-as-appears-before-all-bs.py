class Solution:
    def checkString(self, s: str) -> bool:
        for i, c in enumerate(s):
            if i > 0 and s[i - 1] == 'b' and c == 'a':
                return False
        return True