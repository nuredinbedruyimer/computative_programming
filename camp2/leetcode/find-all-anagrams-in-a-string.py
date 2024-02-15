class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def check(p, s):
            return p==s
        def get_answer():
            # sliding window with window size of len(p)
            Np= len(p)
            Ns = len(s)
            if Np>Ns:
                return []
            p_memo = {}
            s_memo = {}
            for i in range(Np):
                p_memo[p[i]] = 1 + p_memo.get(p[i], 0)
                s_memo[s[i]] = 1 + s_memo.get(s[i], 0)
            ans = []
            
            if check(p_memo, s_memo):
                print("YES")
                ans=[0]
            for i in range(Np,Ns):
                s_memo[s[i-Np]]-=1
                if s_memo[s[i-Np]]==0:
                    del s_memo[s[i-Np]]
                s_memo[s[i]]= 1 + s_memo.get(s[i], 0)
                if check(p_memo,s_memo):
                    ans.append(i-Np+1)
            return ans
        return get_answer()
