class Solution:
  def canJump(self, nums: List[int]) -> bool:
    def get_answer():
        N = len(nums)
        right = N-1
        now = right
        

        while right>=0:
            if right+ nums[right]>=now:
                now = right
            right-=1
            

        return now == 0
    return  get_answer()
 