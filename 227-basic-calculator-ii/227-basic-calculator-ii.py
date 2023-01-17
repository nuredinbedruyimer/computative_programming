class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        operator="+"
        number=0
        length=len(s)
        
        operators=["+","-","*","/"]
        digits=set(str(i) for i in range(10))
        for index in range(len(s)):
            char=s[index]
            if char in digits:
                number=number*10+int(char)
            if char in operators or index==length-1:
                if operator=="+":
                    stack.append(number)
                elif operator=="-":
                    stack.append(-number)
                elif operator=="*":
                    stack[-1]*=number
                elif operator=="/":
                    stack[-1]/=number
                    stack[-1]=int(stack[-1])
                number=0
                operator=char
        result=sum(stack)
        return result
                
                
        