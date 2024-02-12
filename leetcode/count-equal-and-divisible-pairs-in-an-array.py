class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
         def get_answer():
           N = len(nums)
           ans = 0
           for left in range(N):
               for right in range(left+1,N):
                    if nums[right]==nums[left] and (left*right)%k==0:
                         ans+=1
           return ans
         return get_answer()
    