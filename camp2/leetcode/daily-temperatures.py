class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def get_answer():
            N =  len(temperatures)
            ans = [0 for _ in range(N)]
            stack = []
            for i in range(N):
                while stack and  temperatures[stack[-1]]<temperatures[i]:
                    index = stack.pop()
                    ans[index] = i-index



                stack.append(i)
                
            return ans
        return get_answer()
        