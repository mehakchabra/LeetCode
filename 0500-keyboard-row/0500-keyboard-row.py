class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')
        ans=[]
        for i in words:
            y=i[0].lower()
            if y in first_row:
                x=first_row
            elif y in second_row:
                x=second_row
            else:
                x=third_row

            # Using for else loop
            
            for j in i.lower():
                if j not in x:
                    break
            else:ans.append(i)
        return ans