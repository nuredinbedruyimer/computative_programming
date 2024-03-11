def longest_string(s):
    seen = set(s)

    for i in range(len(s)):

        if s[i].lower() in seen  and  s[i].upper() in seen:
            continue

        left = longest_string(s[:i])
        right = longest_string(s[i+1:])

        return max(left, right, key=len)
    
    return s


class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        return longest_string(s)

   