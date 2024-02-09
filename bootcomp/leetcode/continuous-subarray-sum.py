class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap={0:0}
        curr_sum=0
        
        #Store The Last Endex of The remainder for element
        for i in range(len(nums)):
            curr_sum+=nums[i]
           
            if curr_sum%k not in hashmap:
                hashmap[curr_sum%k]=i+1
            elif curr_sum%k in hashmap and hashmap[curr_sum%k]<i:
                return True
        return False
            
        
        
