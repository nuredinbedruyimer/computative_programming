class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2:
            return []
        ans=[]
        
        counter=Counter(changed)
        changed.sort()
        for number in changed:
            if number==0 and counter[number]>=2:
                ans.append(number)
                counter[number]-=2
            if number>0  and counter[number] and counter[2*number]:
                ans.append(number)
                counter[number]-=1
                counter[2*number]-=1
        if len(ans)==len(changed)//2:
            return ans
        return []
        
                
       