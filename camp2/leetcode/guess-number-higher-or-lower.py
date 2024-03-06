# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        low = 0
        high = n

        while low <= high:
            middle =low + (high - low)//2
            if guess(middle) == -1:
                high = middle - 1
            elif guess(middle) == 1:
                low = middle + 1
            elif guess(middle) == 0:
                return middle
        