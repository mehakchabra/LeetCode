class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        w = sentence.split()
        l=[]
        v=[]
        for i in w:
            a = 1*i 
            if(i[0]=='a'or i[0]=='e'or i[0]=='i' or i[0]=='o' or i[0]=='u' or    i[0]=='A'or i[0]=='E'or i[0]=='I' or i[0]=='O' or i[0]=='U'):
                i = i+"ma"
                l.append(i)
            else:
                w = i[1:]+i[0]+"ma"
                l.append(w)
        for i in range(len(l)):
            q = l[i]+"a"*(i+1)
            v.append(q)
        m = " ".join(v)

        
        return m