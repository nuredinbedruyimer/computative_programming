def get_phone_number():
    number_letter_memo = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    return number_letter_memo

    
def letter_combination(digits, number_letter_memo,picked, ans):
    if not digits:
        ans.append(picked)
        return 
    for char in number_letter_memo[digits[0]]:
        letter_combination(digits[1:],number_letter_memo, picked + char, ans )









    


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        #  check for empty 
        if not digits:
            return ans
        #  generate number with letter mapp
        number_letter_memo = get_phone_number()

        letter_combination(digits, number_letter_memo,"", ans)
        return ans
        
        