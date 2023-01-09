class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum=0
        subArrayCounter=0
        for left  in range(k):
            sum+=arr[left]
        testerSum=k*threshold
        if(testerSum<=sum):
            subArrayCounter+=1
        for right in range(k,len(arr)):
            sum-=arr[right-k]
            sum+=arr[right]
            if(testerSum<=sum):
                subArrayCounter+=1
        return subArrayCounter
        
        