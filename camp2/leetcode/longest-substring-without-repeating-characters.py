class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def get_answer():
            max_window = 0
            N = len(s)
            left = 0
            right = 0
            seen = set()
            while right<N:
                while left<N and s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[right])
                max_window = max(max_window, right-left+1)
                right+=1
            return max_window
        return get_answer()


        