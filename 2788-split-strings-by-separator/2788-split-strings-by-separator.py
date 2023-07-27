class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]: 
        words1 =[]
        for word in words:
            for w in word.split(separator):
                if w:  words1.append(w)
        return words1