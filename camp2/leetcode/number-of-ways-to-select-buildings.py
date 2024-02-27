class Solution:
    def numberOfWays(self, s: str) -> int:

                
                    
        def get_answer():

            one = zero = zero_1 = one_0 = 0
            valid_ways = 0

            for char in s:
                if char == '0':
                    zero += 1
                    one_0 += one
                    valid_ways += zero_1
                else:
                    one += 1    
                    zero_1 += zero 
                    valid_ways += one_0
            return valid_ways
           
        return get_answer()
          
            
             

                 

                

        