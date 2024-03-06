def black_box(piles, speed ,  hours_have):
    hours = 0
    for banana in piles:
        hours += math.ceil( banana / speed )
    return hours <= hours_have
    
    

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        
        4,11,20,23,30
        h=5 
        1 2 3 4 5 6 7 8 9
        F F F T T T T T T

        finding first True point
        
        """
        low = 1
        
        high =  max( piles )

        speed = high

        while low <= high:

            middle = ( low + high ) // 2 
            
            if black_box(piles , middle , h):

                speed = min( speed , middle )

                high = middle - 1
            else:

                low = middle + 1

        return speed
                
        
        