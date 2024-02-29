class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        def get_answer(target):
            
            ans = 0
            for i in range(maxDoubles):
                if target == 1:
                    break
                if target % 2 == 0:
                    target = target // 2
                    ans += 1
                else:
                    target = (target - 1) // 2
                    ans += 2

            ans += target-1
            return ans
        return get_answer(target)
