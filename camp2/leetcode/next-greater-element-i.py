class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #  helper function to store the index of nums1 element 
        #  it help to store answer after we find the first greater elemnt in the second num
        def helper():
            N = len(nums1)
            memo = {}

            for i in range(N):
                memo[nums1[i]] = i
            return memo
        def get_answer():
            memo = helper()
       
            ans=[-1]*len(nums1)
        
            stack=[]
            for i in range(len(nums2)):
                curr=nums2[i]
                while stack and curr>stack[-1]:
                    value=stack.pop()
                    index=memo[value]
                    ans[index]=curr
                if curr in memo:
                    stack.append(curr)
            return ans
        return get_answer()
                
        