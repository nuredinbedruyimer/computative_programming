class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        end=len(height)-1
        start=0
        while start<end:
            area=(end-start)*min(height[end],height[start])
            ans=max(ans,area)
            if height[end]<height[start]:
                end=end-1
            else:
                start=start+1
           
        return ans
        