class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length=len(arr)
        ans=[]
        for i in range(length):
            maxValue=max(arr[:length-i])
            maxIndex=arr.index(maxValue)+1
            arr[:maxIndex]=reversed(arr[:maxIndex])
            ans.append(maxIndex)
            arr[:length-i]=reversed(arr[:length-i])
            ans.append(length-i)
        return ans
            
        
       