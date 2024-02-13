class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        def get_answer():

            piles.sort()

            left=0

            right = len(piles)-1

            max_score=0

            while left<right:

                max_score = max_score+piles[right-1]

                left=left+1

                right=right-2

            return max_score

        return get_answer()