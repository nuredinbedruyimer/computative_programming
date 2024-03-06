def get_answer(n):

    low = 0

    high = n

    while low <= high:

        middle = (low + high)//2

        if middle * middle > n:
            high = middle - 1
        else:
            ans = middle
            low = middle + 1
    return ans

class Solution:
    def mySqrt(self, x: int) -> int:

        return get_answer(x)
        