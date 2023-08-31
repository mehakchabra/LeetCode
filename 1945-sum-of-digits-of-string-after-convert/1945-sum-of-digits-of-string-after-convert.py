class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ""
        num = 0
        count =1
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for i in s:
            string += str(alphabets.index(i) + 1)

        for i in string:
            num+=int(i)

        while count<k:
            sum=0
            while num>0:
                sum+=num%10
                num //=10
            num=sum
            count+=1
        return num
        
        