# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        while low<=high:
            middle=(low+high)//2
            value=guess(middle)
            if value==1:
                low=middle+1
            if value==-1:
                high=middle-1
            if value==0:
                return middle
        return n
        
                
                
        