class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=set(allowed)
        n=len(words)
        for word in words:
            for c in word:
                if c not in ans:
                    n-=1
                    break
        return n