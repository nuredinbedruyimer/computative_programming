class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        

        def get_answer():
            ans = 0
            correct_position = 0
            N = len(flips)
            for i in range(N):
                correct_position = max(correct_position, flips[i])
                if correct_position==i+1:
                    ans+=1
            return ans
        return get_answer()

        