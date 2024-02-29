
    

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def get_answer():
            ans_stack =[]
            stack = []
            N = len(s)
            some_flag = False
            ans =  0
            for i in range(N):
                curr = s[i]
                if curr=='(':
                    stack.append(curr)
                    some_flag = True
                elif curr == ')':
                    if some_flag:
                        stack.pop()
                        open_have = len(stack)
                        ans+=2**open_have

                        
                        
                        # do something
                        some_flag = False
                    else:
                        # do something
                        stack.pop()
            return ans
                
            
                    
               
        return get_answer()
        

        