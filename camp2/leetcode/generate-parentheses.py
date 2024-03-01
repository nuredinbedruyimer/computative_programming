def is_valid(parenthesis):
    stack = []
    for i in parenthesis:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if not stack:

        return True
    else:

        return False


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        """
        
        ((()))
        
        """

        ans = []
        def dfs(generated, open, close):
            if open == n  and close == n:
                if is_valid(generated[1:]):
                    
                    ans.append(generated[1:])
                return 
            if open<n and close<n:
                generated.append('(')
                dfs(generated, open+1, close)
                generated.pop()

            if close<open:
                generated.append(')')
                dfs(generated, open, close+1)
                generated.pop()

            # opening part of generatign open must not greater than that of closing and that of n


            
            
        dfs([''], 0, 0)
        true_ans = []
        for i in ans:
            true_ans.append("".join(i))
        return true_ans



        
        