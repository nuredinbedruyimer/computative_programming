class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            result=power(x*x,n//2)
            return x*result if n%2 else result
        result =power(x,abs(n))
        return result if n >0 else 1/result
        
        
       
        
        
        
       
        
        
            
                
                
            
                