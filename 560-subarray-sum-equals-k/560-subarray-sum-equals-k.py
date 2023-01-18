class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        currentSum=0
        prefix={0:1}
        for num in nums:
            currentSum+=num
            differece=currentSum-k
            ans+=prefix.get(differece,0)
            prefix[currentSum]=1+prefix.get(currentSum,0)
        return ans
            
        