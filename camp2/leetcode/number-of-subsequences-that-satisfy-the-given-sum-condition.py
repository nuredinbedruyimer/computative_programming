class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        def power(base, exponent):
            MOD = 1000000000 + 7
            if exponent == 0:
                return 1
            if exponent % 2 == 1:
                return base * power((base * base)%MOD, (exponent - 1) // 2)
            else:
                return power((base * base)%MOD, (exponent) // 2)

        def get_answer():
            MOD = 1000000000 + 7
            nums.sort()
            N = len(nums)
            left = 0
            right = N - 1
            ans = 0
            while right >= left:
                if nums[right] + nums[left] > target:
                    right -= 1
                else:
                    ans += power(2, right - left)
                    left += 1

            return ans % MOD

        return get_answer()
