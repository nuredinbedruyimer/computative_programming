class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length=len(nums)
        hasCatch=[[False]*(length+1) for i in range(length+1)]
        catch=[[None]*(length+1) for i in range(length+1)]
        def getScore(left,right):
            if left>right:
                return 0
            if hasCatch[left][right]:
                return catch[left][right]
            leftScore=nums[left]-getScore(left+1,right)
            rightScore=nums[right]-getScore(left,right-1)
            hasCatch[left][right]=True
            catch[left][right]=max(leftScore,rightScore)
            return catch[left][right]
        return getScore(0,length-1)>=0
        
        
        