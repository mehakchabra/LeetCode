class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing = []
        for num in range(left,right+1):
            n = num
            while num > 0:
                d = num % 10
                if d == 0:
                    break
                elif n % d != 0:
                    break
                num //= 10
            if num == 0:
                self_dividing.append(n)
        return self_dividing


                
        
            

        
        
                        
                    
                    

