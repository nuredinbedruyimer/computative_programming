class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        def get_answer():
            remainder = sum(nums) % p
            if remainder == 0:
                return 0
            N = len(nums)

            memo = {0: -1}
            current_mod = 0
            min_length = len(nums)
        
            for index in range(N):
                current_mod = (current_mod + nums[index]) % p
                # we just find compliment of modulo because our target is to find
                # subarray with sum divisible by p then our module should be 
                #   modulo = p*m  m= 0, 1, 2, ..... in this case our subarray is divisible by p
                # our target is to remove the  sub array that have total remainder  of out total remainder after that we have pure array with divisible by p
                compliment_mod = (current_mod - remainder + p) % p
            
                if compliment_mod in memo:
                    min_length = min(min_length, index - memo[compliment_mod])
                memo[current_mod] = index
        
            return -1 if min_length == len(nums) else min_length
        return get_answer()
        