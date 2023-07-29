class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        list(sentence)
        if len(sentence)<26:
            return False
        for alphabet in alphabets:
            if alphabet not in sentence:
                return False
        return True

        