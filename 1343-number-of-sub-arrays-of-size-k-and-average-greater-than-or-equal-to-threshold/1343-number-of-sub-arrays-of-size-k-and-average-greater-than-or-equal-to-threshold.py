class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum=0
        counter=0
        for i  in range(k):
            sum+=arr[i]
        testerSum=k*threshold
        if(testerSum<=sum):
            counter+=1
        for j in range(k,len(arr)):
            sum+=arr[j]
            sum-=arr[j-k]
            if(testerSum<=sum):
                counter+=1
        return counter
        
        