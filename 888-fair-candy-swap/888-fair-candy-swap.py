class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        sumOne=sum(aliceSizes)
        sumTwo=sum(bobSizes)
        difference=(sumOne-sumTwo)//2
        numOne=set(aliceSizes)
        for value in bobSizes:
            if (value+difference) in numOne:
                return[value+difference,value]
        
        