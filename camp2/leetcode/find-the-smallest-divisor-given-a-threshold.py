import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def black_box(mid,nums,t):
            total=0
            for num in nums:
                total+=math.ceil(num/mid)
            return total<=t
                
        def min_divisor(nums,t):
            low=1
            high=max(nums)
            while low<=high:
                middle=(low+high)//2
                
                if black_box(middle,nums,t):
                    ans=middle
                    high=middle-1
                else:
                    low=middle+1
            return ans
        return min_divisor(nums,threshold)
        