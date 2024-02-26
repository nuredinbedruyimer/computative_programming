class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permutation(stack):
            if len(stack)==len(nums):
                ans.append(stack[:])
                return 
            for a in nums:
                if a not in stack:
                    stack.append(a)
                    permutation(stack)
                    stack.pop()
        permutation([])
        return ans
            
                    

         
        
       