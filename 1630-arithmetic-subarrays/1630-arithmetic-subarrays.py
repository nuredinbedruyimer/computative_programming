class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        N=len(nums)
        def isGood(left,right):
            sortedList=list(sorted(nums[left:right+1]))
            if len(sortedList)==1:
                return True
            change=sortedList[1]-sortedList[0]
            for a,b in zip(sortedList,sortedList[1:]):
                if b-a!=change:
                    return False
            return True
        ans=[]
        for left,right in zip(l,r):
            ans+=[isGood(left,right)]
        return ans
            
        