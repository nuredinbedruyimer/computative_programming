class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOnes=0
        left=0
        for right,num in enumerate(nums):
            k=k-1+num # binary number
            if(k<0):
                k+=1-nums[left]
                left=left+1
            else:
                maxOnes=max(maxOnes,right-left+1)
        return maxOnes
        