class Solution:
    def longestPalindrome(self, s: str) -> int:
       
        def get_answer():
            memo = {}
            N= len(s)
            max_odd_freq = 0
            flag = True
            for i in s:
                memo[i] = 1 + memo.get(i, 0)
            if len(memo)==1:
                return N
            ans = 0
            for char in memo:
                if memo[char]%2==0:
                    ans+=memo[char]
                elif memo[char] and flag:
                    flag = False
                    ans+=memo[char]
                else:
                    ans+=memo[char]-1
            return ans
        return get_answer()
                

                


            
        