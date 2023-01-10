class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result=0
        counter={}
        for num in nums:
            temp=k-num
            if temp in counter and counter[temp]>0:
                result+=1
                counter[temp]-=1
            else:
                if num  not in counter:
                    counter[num]=0
                counter[num]+=1
        return result
        
        