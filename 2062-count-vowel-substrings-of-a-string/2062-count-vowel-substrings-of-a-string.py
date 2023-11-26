class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        fin=0
        for i in range(len(word)):             
            res = set()
            for j in range(i,len(word)):
                if word[j] in 'aeiou':
                    res.add(word[j])
                    if len(res)>=5:
                        fin+=1
                else:
                    break                
        return fin