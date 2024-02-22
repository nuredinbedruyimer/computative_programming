class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def get_answer():
            left, right = 0, 0
            N = len(name)
            T=len(typed)
            while right < T:

                if left < len(name) and name[left] == typed[right]:
                    left += 1
                    right += 1
                elif right > 0 and typed[right-1] == typed[right]:
                    right += 1
                else:
                    return False

            return left == N
        return get_answer()