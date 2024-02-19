class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        making the intersection point to be largest possible value 
        and fill the others with larger value as well
        
        """
        def get_answer():
            N = len(nums)
            store = [0 for _ in range(N+1)]
            for start, end  in requests:
                store[start]+=1
                store[end+1]-=1
            prefix_sum= [store[0]]
            for i in range(1, N):
                prefix_sum.append(store[i]+prefix_sum[-1])
            nums.sort(reverse=True)
            prefix_sum.sort(reverse=True)
            ans = 0
            for i in range(N):
                ans +=prefix_sum[i]*nums[i]
            MOD = 10**9+7
            return ans%MOD
        return get_answer()

            
          
            

        