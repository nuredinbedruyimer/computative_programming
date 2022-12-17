class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        result=[]
        frequency=[[] for i in range(len(nums)+1)]
        for num in nums:
            counter[num]=1+ counter.get(num,0)
        for num , counter in counter.items():
            frequency[counter].append(num)
        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                result.append(num)
                if len(result)==k:
                    return result
       