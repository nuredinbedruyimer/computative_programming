class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combSum(index,stack,target,ans,length):
            if index == length:
                if target==0:
                    ans.append(stack[:])
                    
                    
                return
            if candidates[index]<=target:
                stack.append(candidates[index])
                combSum(index,stack,target-candidates[index],ans,length)
                stack.pop()
            combSum(index+1,stack,target,ans,length)
        ans=[]
        stack=[]
        combSum(0,stack,target,ans,len(candidates))
        return ans
            

            
            
                
            
        