class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub_set(index, arr, length, stack,ans):
            if index >= length:
                ans.append(stack[:])
                return
            stack.append(arr[index])
            sub_set(index+1, arr, length, stack,ans)
            stack.pop()
            sub_set(index+1, arr, length, stack,ans)
        stack=[]
        ans=[]    
        sub_set(0, nums,len(nums),stack,ans)
        
        return ans
        
        