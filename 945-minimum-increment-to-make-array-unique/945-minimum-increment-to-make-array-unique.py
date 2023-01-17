class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        stack=[nums[0]]
        ans,preValue=0,nums[0]
        length=len(nums)
       
        for index in range(1,length):
            currentValue=nums[index]
            if currentValue<=preValue:
                ans +=preValue-currentValue+1
                currentValue=preValue+1
            stack.append(currentValue)
           
            preValue=currentValue
        return ans
       
        
        