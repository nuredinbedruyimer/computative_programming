class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base, exponent):
            if exponent==0:
                return 1
            if exponent%2==1:
                return base*power(base*base, (exponent-1)//2)
            else:
                return power(base*base, exponent//2)

        def get_answer():
            return power(x, n) if n>0 else 1/power(x, abs(n)) 
        return get_answer()

        