class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        settedChar=set()
        print(settedChar)
        
        maxCounter=0
        for right in range(len(s)):
            while s[right] in settedChar:
                settedChar.remove(s[left])
                left=left+1
            settedChar.add(s[right])
            maxCounter=max(maxCounter,right-left+1)
        return maxCounter
            
        