class Solution:
    def balancedString(self, s: str) -> int:
        def is_valid(memo):
            for char in "QWRE":
                if len(s)//4>=memo[char]:
                    continue
                else:
                    return False
            return True
        def get_answer():
            memo = defaultdict(int)
            for i in s:
                memo[i]+=1

            start,ans = 0, len(s)
            for end in range(len(s)):
                memo[s[end]] -= 1
                while start < len(s) and is_valid(memo):
                    ans = min(ans,end-start+1)
                    memo[s[start]] += 1
                    start += 1
            return ans
        return get_answer()


        
        
        