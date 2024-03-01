def power(n):

    if n == 1:
        return True
    
    if n == 0 or n % 3 != 0:
        return False
    

    return power(n // 3)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return power(n)

        