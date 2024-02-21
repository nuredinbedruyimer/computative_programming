class Solution:
    def fib(self, n: int) -> int:
        # Method One Using Recursion
        def get_answer_one(n):
            if n<2:
                return n
            return  get_answer_one(n-1)+get_answer_one(n-2)
        # Method two using topdown momiazation(dp)
        dp = [-1 for _ in range(n+1)]
        def get_answer_two(n):
            if n<2:
                return n
            if dp[n]!=-1:
                return dp[n]
            dp[n] = get_answer_one(n-1)+get_answer_one(n-2)
            return dp[n]
        # Method Three using tabulation 
        def get_answer_three():
            dp = [0 for _ in range(n+1)]
            if n==0:
                return 0
            dp[0] = 0
            dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1]+dp[i-2]
            return dp[n]
        return get_answer_three()
        
        




        # Method Four space optimazed Dp solution
        def get_answer_fout():
            first = 0
            second = 1
            if n==0:
                return 0



            for i in range(2, n+1):
                temp =first
                first = second 
                second= temp+second
            return second

        
        