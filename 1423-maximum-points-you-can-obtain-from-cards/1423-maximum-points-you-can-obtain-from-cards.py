class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pointOne=0
        right=len(cardPoints)-k
        left=0
        for i in range(len(cardPoints)-k,len(cardPoints)):
            pointOne+=cardPoints[i]
        maxPoint=pointOne
        print(right)
        while right<len(cardPoints):
            pointOne=pointOne+cardPoints[left]-cardPoints[right]
            maxPoint=max(pointOne,maxPoint)
            left=left+1
            right=right+1
        return maxPoint
        
            
            
        