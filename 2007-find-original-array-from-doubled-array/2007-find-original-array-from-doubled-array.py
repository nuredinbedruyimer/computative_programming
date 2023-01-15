class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2:
            return []
        ans=[]
        
        counter=Counter(changed)
        changed.sort()
        for i in changed:
            if i==0 and counter[i]>=2:
                ans.append(i)
                counter[i]-=2
            if i>0  and counter[i] and counter[2*i]:
                ans.append(i)
                counter[i]-=1
                counter[2*i]-=1
        if len(ans)==len(changed)//2:
            return ans
        return []
        
                
       