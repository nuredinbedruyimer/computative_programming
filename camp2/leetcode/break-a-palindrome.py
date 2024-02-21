class Solution:
    def breakPalindrome(self, s: str) -> str:
        s= list(s)
        def get_answer():
            n = len(s)
            if n ==1:
                return ""
            ans = [s[n//2]]*n
            is_changed = False
            for i in range((n)//2):
                if not is_changed and s[i]!='a':
                    ans[i]='a'
                    is_changed = True
                else:
                    ans[i]=s[i]
                ans[n-i-1]=s[i]
            if is_changed:
                return "".join(ans)
            else:
                
                s[-1] = 'b'
                return "".join(s)
        return get_answer()
            
        """
        abbba
        abccba
        
        """
        