class Solution:
    def swapNumber(self, nums, index1 , index2):
        temp=nums[index1]
        nums[index1]=nums[index2]
        nums[index2]=temp
    def reverseNum(self ,nums,left,right):
        while left<right:
            self.swapNumber(nums,left,right)
            left=left+1
            right=right-1
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums)==1:
            return
        if len(nums)==2:
            return self.swapNumber(nums,0,1)
        dec=len(nums)-2
        while dec>=0 and nums[dec]>=nums[dec+1]:
            dec=dec-1
        self.reverseNum(nums,dec+1,len(nums)-1)
        if dec==-1:
            return
        nextNum=dec+1
        while nextNum<len(nums)and nums[nextNum]<=nums[dec]:
            nextNum=nextNum+1
        self.swapNumber(nums,nextNum,dec)
        
    
    
        
        
        