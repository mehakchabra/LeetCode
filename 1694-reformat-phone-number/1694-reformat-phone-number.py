class Solution:
    def reformatNumber(self, number: str) -> str:
        res=[]
        new=""
        for i in number:
            if i!=" " and i!="-":
                res.append(i)
        n=len(res)
        while(n>4):
            s="".join(res[:3])
            res=res[3:]
            n-=3
            new=new+s+"-"
        if len(res)==3 or len(res)==2:
            new=new+"".join(res)
        if len(res)==4:
            s1="".join(res[:2])
            s2="".join(res[2:])
            new=new+s1+"-"+s2
        return new