class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        intList=[]
        for i in range(len(nums)):
            n=int(nums[i])
            intList.append(n)
        intList.sort()
        return str(intList[len(nums)-k])
       
    
    
    
    
    
    
    
       
        
            
    
            
        
        