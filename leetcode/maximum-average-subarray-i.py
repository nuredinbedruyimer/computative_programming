class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def get_answer():
            N= len(nums)
            total = sum(nums[:k])
            ans =total /k
            left = 0
            for i in range(k,N):
                total-=nums[left]
                total+=nums[i]
                ans = max(ans, total/k)
                left+=1
            return ans
        return get_answer()



        