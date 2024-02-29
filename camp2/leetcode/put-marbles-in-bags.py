class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        def get_answer():
            """
            1 3 5 1
            [4, 8, 6]
            [4, 6, 8]
            to obtau=in the max take 
            
            
            """
            N=len(weights)
            if N==k:
                return 0

            bags = [0 for _ in range(N-1)]
            for i in range(N-1):
                bags[i] = weights[i]+ weights[i+1]
            bags.sort()
            max_marbles = 0
            for i in range(N-k, N-1):
                max_marbles+=bags[i]
            min_marbles = 0
            for i in range(k-1):
                min_marbles+=bags[i]
            ans = max_marbles - min_marbles
            return ans
        return get_answer()
        