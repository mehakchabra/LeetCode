class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt = 0
        for w in words1:
            if words1.count(w)==1 and words2.count(w)==1:
                cnt += 1
        return cnt
        