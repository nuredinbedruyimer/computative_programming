class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def get_answer(k):
            max_ones=0
            left=0
            for right in range(len(nums)):
                k=k-1+nums[right] # binary number
                # shrinking our window when we get more than k zeros
                if(k<0):
                    k+=1-nums[left]
                    left=left+1
                else:
                    max_ones=max(max_ones,right-left+1)
            return max_ones

        return get_answer(k)
        
        