class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        score_a = [0]
        score_b = [0]
        def dfs(nums, is_player_one):
            if not nums:
                return 0

            if is_player_one:
                left  =  nums[-1] + dfs(nums[:-1], not is_player_one)
                right =  nums[0] + dfs(nums[1:], not is_player_one)
                return max(left, right)
            else:
                left  =  -nums[-1] + dfs(nums[:-1], not is_player_one)
                right =  -nums[0] + dfs(nums[1:], not is_player_one)
                return min(left, right)
            
        return dfs(nums, True)>=0

        