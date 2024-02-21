class Solution:
    def isValid(self, s: str) -> bool:
        def get_answer():
            N = len(s)
            openes= {'}':'{',']':'[', ')':'(' }
            stack = []
            for i in range(N):
                # "([])"
                # if it is opening parenthesis add to the stack 
                if s[i]=='(' or s[i]=='{' or s[i]=='[':
                    stack.append(s[i])
                else:
                    if not stack:
                        return False
                    symbol = stack.pop()
                    if symbol == openes[s[i]]:
                        continue
                    else:
                        return False
            return True if not stack else False
        return get_answer()
        