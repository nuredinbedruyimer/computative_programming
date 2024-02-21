class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def get_reverse(left, right):
            if left>=right:
                return 
            s[left], s[right] = s[right], s[left]
            get_reverse(left+1, right-1)
        get_reverse(0, len(s)-1)
        