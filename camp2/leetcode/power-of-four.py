def power(n):
    if n == 1:
        return True
    
    if n % 4 != 0 or n == 0:
        return False

    return power(n//4)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        return power(n)
        