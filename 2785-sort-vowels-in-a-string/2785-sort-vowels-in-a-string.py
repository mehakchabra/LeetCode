
class Solution:
    def isVowel(self, c):
        return c.lower() in ['a', 'e', 'i', 'o', 'u']

    def sortVowels(self, s):
        t = ""        
        temp = ""     

        for char in s:
            if self.isVowel(char):
                temp += char

        temp = ''.join(sorted(temp))

        j = 0
        
        for char in s:
            if self.isVowel(char):
                t += temp[j]
                j += 1
            else:
                t += char

        return t
