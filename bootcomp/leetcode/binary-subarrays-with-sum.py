
  


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        [1,0,1,0,1]
        """
        1: 0
        1:1
        2:2

        
        """
        def get_answer(goal):
            N = len(nums)
            left = counter = ans = 0
            for right in range(N):
                if nums[right] == 1:
                    goal -= 1
                    counter = 0
                while goal < 0:
                    goal += nums[left]
                    left += 1
                while goal == 0 and left <= right:
                    goal += nums[left]
                    left += 1
                    counter += 1
                ans += counter
            return ans
        return get_answer(goal)


