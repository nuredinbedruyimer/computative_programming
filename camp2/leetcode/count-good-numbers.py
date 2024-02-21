class Solution:
    def countGoodNumbers(self, n: int) -> int:
       

        def power(base, exponent):
            MOD = 1000000000+7
            if exponent==0:
                return 1
            if exponent%2==0:
                return power((base*base)%MOD, exponent//2)
            else:
                return base*power((base*base)%MOD, (exponent-1)//2)
        def get_answer():
            MOD = 1000000000+7
            exponent_of_four = n//2
            exponent_of_five = n//2 + 1 if n%2==1 else n//2
            return power(5, exponent_of_five)%MOD * power(4, exponent_of_four)%MOD
        return get_answer()
        
        