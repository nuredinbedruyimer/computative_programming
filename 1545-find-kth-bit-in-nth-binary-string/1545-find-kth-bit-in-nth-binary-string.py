class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def getReverse(s):
            ans=[]
            for i in s:
                if i=="0":
                    ans.append("1")
                else:
                    ans.append("0")
            return "".join(reversed(ans))
        s="0"
        for i  in range(n):
            s=s+"1"+getReverse(s)
        return s[k-1]
        