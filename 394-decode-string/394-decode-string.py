class Solution:
    def decodeString(self, s: str) -> str:
        resultStack=[]
        for index in range(len(s)):
            if(s[index]!="]"):
                resultStack.append(s[index])
            else:
                substr=""
                while resultStack[-1]!="[":
                    substr=resultStack.pop() + substr
                resultStack.pop()
                number=""
                while resultStack and resultStack[-1].isdigit():
                    number=resultStack.pop()+number
                    print(number)
                resultStack.append(int(number)*substr)
        print(resultStack)
        result ="".join(resultStack)
        return result
                
                    
        