class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        list(words)
        string = ""
        for word in words:
            new_word = word[::-1]
            if word == new_word:
                string = word
                break
        return string