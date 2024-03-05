def get_answer(matrix, target):
        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(1, n):
                matrix[row][col] += matrix[row][col - 1]
        

        ans = 0
        

        for c1 in range(n):
            for c2 in range(c1, n):
                prefix_sum_count = defaultdict(int)
                prefix_sum_count[0] = 1
                sum_val = 0

                for row in range(m):
                    if c1>0:
                        sum_val += matrix[row][c2] - matrix[row][c1 - 1]  
                    else:
                        sum_val += matrix[row][c2] -  0

                    ans += prefix_sum_count[sum_val - target]
                    
                    prefix_sum_count[sum_val] = prefix_sum_count[sum_val] + 1

        return ans


class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        return get_answer(matrix, target)

