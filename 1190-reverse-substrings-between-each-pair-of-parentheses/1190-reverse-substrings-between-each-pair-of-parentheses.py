class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        i=0
        while(i<len(s)):
            if(s[i]!=")"):
                stack.append(s[i])
            else:
                temp=[]
                while(stack[-1]!="("):
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            i+=1
        return "".join(stack)
        