
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_answer():
            hashmap = {}
            left = 0
            right = 0
            ans = float('-inf')
            for i in s:
                hashmap[i] = 0
                max_character_from_window = 0
            while right < len(s):
                hashmap[s[right]] = 1 + hashmap.get(s[right], 0)
                max_character_from_window = max(max_character_from_window, hashmap[s[right]])
                window = right - left + 1
                _need_replace = window-max_character_from_window
                if _need_replace <= k:
                    ans = max(window, ans)
                else:
                    hashmap[s[left]]-=1
                    left = left + 1
                right = right + 1
            return ans
        return get_answer()


        