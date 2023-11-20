class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        v = ['a', 'e', 'i', 'o', 'u']
        ans = 0
        for i in words[left : right + 1]:
            if i[0] in v and i[-1] in v:
                ans += 1
        return ans