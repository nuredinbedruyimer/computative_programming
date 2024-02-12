class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_valid():
            ans=""
            for i in range(len(s)):
                if s[i].isalnum():
                    ans+=s[i]
                else:
                    continue
            return ans.lower()==ans[::-1].lower()
        return is_valid()
        