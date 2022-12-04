class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        newList=sorted(nums)
        for i in range(len(nums)):
            for j in range(len(newList)):
                if(nums[i]==newList[j]):
                    result.append(j)
                    break
        return result
                    
                    
        