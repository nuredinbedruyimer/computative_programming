class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD=10**9+7
        top=pow(2,p,MOD)-1
        middle=top-1
        midCounter=pow(2,p-1)-1
        return (pow(middle,midCounter,MOD)*top)%MOD
        