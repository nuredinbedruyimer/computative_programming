class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
        def get_answer():
            N = len(nums)
            nums.sort()
            left = 1
            right = N-2
            chemistry = nums[-1]+nums[0]
            ans =nums[0]*nums[-1]
            while left<=right:
                if chemistry==nums[right]+nums[left]:
                    ans+=nums[right]*nums[left]
                    right-=1
                    left+=1
                else:
                    return -1
            return ans
        return get_answer()
                

        