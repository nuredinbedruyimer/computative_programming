class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left,right=0,len(piles)-1
        maxCoin=0
        while left<right:
            maxCoin=maxCoin+piles[right-1]
            left=left+1
            right=right-2
        return maxCoin