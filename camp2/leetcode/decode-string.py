def is_digit(char):

    return char.isdigit()


def decode_string(word):

    stack = []

    N = len(word)

    for i in range(N):

        if word[i] != ']':

            stack.append(word[i])
        
        else:

            letters = ""

            while stack and stack[-1] != '[':
                letters = stack.pop() + letters 
            
            stack.pop()
            
            digit = ""

            while stack and is_digit(stack[-1]):
                digit = stack.pop() + digit
            print(letters)
            
            stack.append(int(digit) * letters)
            
    return "".join(stack)



        


class Solution:
    def decodeString(self, s: str) -> str:

        return decode_string(s)

                
                    
        