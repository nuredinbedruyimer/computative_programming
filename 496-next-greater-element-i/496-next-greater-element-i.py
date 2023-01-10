class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hashmap
        numOneIndex={value:index for index,value in enumerate(nums1)}
       
        ans=[-1]*len(nums1)
       
        stack=[]
        for i in range(len(nums2)):
            currentValue=nums2[i]
            while stack and currentValue>stack[-1]:
                value=stack.pop()
                index=numOneIndex[value]
                ans[index]=currentValue
            if currentValue in numOneIndex:
                stack.append(currentValue)
        return ans
                
        