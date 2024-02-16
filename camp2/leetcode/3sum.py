class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
            

            

        def get_answer(target):
            N = len(nums)
            nums.sort()
            ans = set()
            #  -4 -1 -1 0 1 2
            # -1

            for i in range(N):
                need = target-nums[i]
                left = i+1
                right = N-1
                curr_sum = 0
                while left<right:
                    curr_sum = nums[left]+nums[right]
                    if curr_sum>need:
                        right-=1
                    elif curr_sum<need:
                        left+=1
                    else:
                        ans.add(tuple([nums[i], nums[left], nums[right]]))
                        right-=1
                        left+=1


            return list(ans)
        return get_answer(0)
        