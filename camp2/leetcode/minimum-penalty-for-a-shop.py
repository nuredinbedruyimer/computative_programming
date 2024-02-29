class Solution:
    def bestClosingTime(self, customers: str) -> int:
        def get_answer():
            N = len(customers)
            yes_memo = [0 for _ in range(N+1)]
            no_memo = [0 for _ in range(N+1)]
            for i in range(N):
                if customers[i]=='N':
                    no_memo[i+1]= no_memo[i] + 1
                else:
                    no_memo[i+1] = no_memo[i] 
            for i in range(N-1, -1, -1):
                if customers[i]=='Y':
                    yes_memo[i] =yes_memo[i+1]+1
                else:
                    yes_memo[i] = yes_memo[i+1]
            prefix_sum = [0 for _ in range(N+1)
            ]
            for i in range(N+1):

                prefix_sum[i] = no_memo[i]+yes_memo[i]
            min_value = float('inf')
            min_index = -1
            for i in range(N+1):
                if prefix_sum[i]<min_value:
                    min_index = i
                    min_value = prefix_sum[i]
            return min_index
            

        return get_answer()

     