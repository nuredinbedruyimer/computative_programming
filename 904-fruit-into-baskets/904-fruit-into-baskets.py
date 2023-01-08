class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        left=0
        maxFruit=0
        counter=defaultdict(int)    
        for right,fre in enumerate(fruits):
            counter[fre]+=1
            while len(counter)>2:
                counter[fruits[left]]-=1
                if counter[fruits[left]]==0:
                    del counter[fruits[left]]
                left=left+1
            maxFruit=max(maxFruit,right-left+1)
        return maxFruit
        