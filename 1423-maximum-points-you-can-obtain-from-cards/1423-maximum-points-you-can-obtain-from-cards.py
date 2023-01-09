class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pointOne=0
        right=len(cardPoints)-k
        
        for left in range(k):
            pointOne+=cardPoints[left]
        maxPoint=pointOne
        print(pointOne)
        print(left)
        right=len(cardPoints)-1
        while left>=0:
            pointOne=pointOne-cardPoints[left]+cardPoints[right]
            maxPoint=max(pointOne,maxPoint)
            left=left-1
            right=right-1
        return maxPoint
        
            
            
        