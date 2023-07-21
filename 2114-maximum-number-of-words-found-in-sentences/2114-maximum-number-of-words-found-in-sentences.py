class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_spaces = 0
        for i in range(0,len(sentences)):
            spaces = sentences[i].count(" ")
            if max_spaces < spaces:
                max_spaces = spaces
        return max_spaces+1