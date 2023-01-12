class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length=len(arr)
        counter=0
        frequencyCounter=Counter(arr)
        ans=0
        for index,value in sorted(frequencyCounter.items(),key=lambda value:-value[1]):
            counter+=value
            ans+=1
            if counter>=(length//2):
                break
        return ans
            
            
        
        
            
        