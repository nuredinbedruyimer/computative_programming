class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        x={")":"(","]":"[","}":"{"}
        for value in s:
            if value in x:
                if stack and stack[-1]==x[value]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(value)
        return True if not stack else False
        