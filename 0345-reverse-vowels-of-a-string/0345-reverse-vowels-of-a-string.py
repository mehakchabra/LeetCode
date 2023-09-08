class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'
        vowel = list(vowel)
        rev = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowel:
                rev.append(s[i])
                s[i] = '_'
        rev = rev[::-1]
        j=0
        for i in range(len(s)):
            if s[i] == '_':
                s[i] = rev[j]
                j+=1
        return ''.join(s)



        


        