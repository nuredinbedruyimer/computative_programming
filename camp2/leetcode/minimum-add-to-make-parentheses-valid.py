class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        def get_answer():
            stack =[]
           
            for i in s:
                if i=='(':
                   stack.append(i)
                else:
                    if stack  and stack[-1]=='(':
                        stack.pop()
                    else:
                        stack.append(i)
            return len(stack)
        return get_answer()
        