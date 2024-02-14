class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        right = 0
        s=list(s)
        operation = 0
        while right < len(s):
        
            if s[right]=='1':
                pass
            elif s[right] == '0':
                s[right], s[left] = s[left], s[right]
                operation+=right-left
                left+=1
                
            right+=1
        return operation
        