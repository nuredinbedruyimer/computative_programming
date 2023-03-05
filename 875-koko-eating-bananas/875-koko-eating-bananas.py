class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """4,11,20,23,30
        h=5 """
        left=1
        right=max(piles)
        time=right
        while left<=right:
            middle=(left+right)//2
            numberOfHour=0
            for banana in piles:
                numberOfHour+=math.ceil(banana/middle)
            if numberOfHour<=h:
                time=min(time,middle)
                right=middle-1
            else:
                left=middle+1
        return time
                
        
        