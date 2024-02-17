class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        def get_answer():
            _sum = 0
            _max = 0
            left=0
            ans = float('-inf')
            seen =set()
            for   right in range(len(nums)):
                _sum+=nums[right]
                while nums[right] in seen:
                    _sum-=nums[left]
                    seen.remove(nums[left])
                    left+=1
                ans = max(ans, _sum)
                seen.add(nums[right])
            return ans
        return get_answer()
        