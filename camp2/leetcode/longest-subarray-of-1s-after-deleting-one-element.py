class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if nums.count(0)==0:
            return N-1
        def get_answer():
            
            one = 0
            two = 0
            ans = 0
            for i in range(N):
                if nums[i]==1:
                    one+=1
                else:
                
                    for j in range(i+1,N):
                        if nums[j]==1:
                            two+=1
                        else:
                            break
                    ans = max(one+two, ans)
                    one = 0
                    two = 0
            return ans
        return get_answer()

                
        