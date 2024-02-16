class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def get_answer():
            current = 0

            vowels = "aeiou"
            max_window = 0
            for i in range(k):
                if s[i] in vowels:
                    current += 1
            max_window = max(max_window, current)
            left = 0
            for i in range(k, len(s)):
                if s[left] in vowels:
                    current -= 1
                    left += 1
                else:
                    left += 1
                if s[i] in vowels:
                    current += 1

                max_window = max(max_window, current)
            return max_window

        return get_answer()
