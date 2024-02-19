class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def get_answer():
            N=len(fruits)
            left=0
            max_fruit=0
            counter=defaultdict(int)    
            for right,fre in enumerate(fruits):
                counter[fre]+=1
                while len(counter)>2:
                    counter[fruits[left]]-=1
                    if counter[fruits[left]]==0:
                        del counter[fruits[left]]
                    left=left+1
                max_fruit=max(max_fruit,right-left+1)
            return max_fruit
        return get_answer()
      
        