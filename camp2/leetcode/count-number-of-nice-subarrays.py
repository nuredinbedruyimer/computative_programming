class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def get_answer(k):
            left = 0
            even_counter = 0
            right = 0
            ans = 0
            N = len(nums)
            while right < N:
                if nums[right] % 2 == 1:
                    k = k - 1
                    even_counter = 0
                while k == 0:
                    if nums[left] % 2 == 1:
                        k = k + 1

                    left += 1
                    even_counter += 1
                ans += even_counter
                right = right + 1
            return ans

        return get_answer(k)
