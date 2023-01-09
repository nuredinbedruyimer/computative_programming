class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endIndexs={}
        for currentIndex ,element in enumerate(s):
            endIndexs[element]=currentIndex
        endIndex=0
        sizeOfPartition=0
        ans=[]
        for currentIndex,element in enumerate(s):
            sizeOfPartition+=1
            endIndex=max(endIndex,endIndexs[element])
            
            
            if currentIndex==endIndex:
                ans.append(sizeOfPartition)
                sizeOfPartition=0
        return ans
            
            
        
        