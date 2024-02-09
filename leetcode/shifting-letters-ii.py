class Solution:
    def shiftingLetters(self, s: str, arr: List[List[int]]) -> str:
        def get_answer(s,arr):
            N= len(s)
            shifts = [0 for _ in range(N+1)]
            
            for start, end, value  in arr:
                
                if value == 0:
                    shifts[start] -= 1
                    shifts[end+1] += 1
                else:
                    shifts[start] += 1
                    shifts[end+1] -= 1
            print(shifts)
            
            cur_sum = 0
            for i in range(len(s)):
                cur_sum += shifts[i]
                
                letter_ascii = (((ord(s[i]) + cur_sum) - 97) % 26) + 97
                s = s[:i] + chr(letter_ascii) + s[i+1:]
            
            return s
        return get_answer(s,arr)
        