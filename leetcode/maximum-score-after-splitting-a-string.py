class Solution:
    def maxScore(self, s: str) -> int:
        def get_answer():
            N= len(s)
            ans = float('-inf')
            one = 0
            zero = 0
            for i in range(N-1):
                if s[i]=='1':
                    one+=1
                else:
                    zero+=1
                ans = max(ans,zero-one) 
            one = one + int(s[-1])
            return ans + one
        return get_answer()
        