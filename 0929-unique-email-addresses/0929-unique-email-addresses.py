class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        arr=[]
        for i in emails:
            if '@' in i:
                at = i.index('@')
                temp=i[:at]
                temp=temp.replace(".","")
                
                if '+' in temp:
                    plus = temp.index('+')
                    temp = temp[0:plus]
                temp+=i[at:]
                if temp not in arr:
                    arr.append(temp)
            else:
                continue
        return len(arr)