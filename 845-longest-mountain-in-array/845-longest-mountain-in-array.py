class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        heights={}
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                heights[i]=arr[i]
        right=0
        left=0
        maxHeight=0
        for i, j in heights.items():
            left=i-1
            while left>0 and arr[left-1]<arr[left]:
                left=left-1
            right=i+1
            while right<len(arr)-1 and arr[right]>arr[right+1]:
                right=right+1
            maxHeight=max(maxHeight,right-left+1)
        return maxHeight
                
            
        