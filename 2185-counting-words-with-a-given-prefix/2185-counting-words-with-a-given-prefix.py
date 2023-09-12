class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for s in words:
            if s.startswith(pref):
                cnt += 1
        return cnt