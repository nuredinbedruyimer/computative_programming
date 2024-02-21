class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def get_answer():
            stack=[]
            for symbol in tokens:
                if symbol=="+":
                    stack.append(stack.pop()+stack.pop())
                elif symbol=="-":
                    top1,top2=stack.pop(),stack.pop()
                    stack.append(top2-top1)
                elif symbol=="*":
                    stack.append(stack.pop()*stack.pop())
                elif symbol=="/":
                    top1,top2=stack.pop(),stack.pop()
                    stack.append(int(top2/top1))
                else:
                    stack.append(int(symbol))
            print(stack)
            return stack[-1]
        return get_answer()


            
            
        