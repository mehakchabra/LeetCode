class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = {}
        result = []
        str1 = s1.split()
        str2 = s2.split()
        for i in str1 + str2:
            freq[i] = freq.get(i,0) + 1
        for i in freq:
            if freq[i] == 1:
                result.append(i)
        return result
            
        
        