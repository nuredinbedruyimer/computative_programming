class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        stack=[]
        nums.sort()
        def sub_set(index, stack,ans):
            ans.append(stack[:])
            for i in range(index,len(nums)):
                if i != index and nums[i]==nums[i-1]:
                    continue
                stack.append(nums[i])
                sub_set(i+1,stack,ans)
                stack.pop()
        sub_set(0,stack,ans)
        return ans
            
        