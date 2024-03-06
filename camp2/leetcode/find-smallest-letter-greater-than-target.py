# def get_answer(letter, target):
#     for i in letter:
#         if i>target:
#             return i
#     return letter[0]
#  time O(n) space O(1)

def get_answer_2(letter, target):

    low =  0 

    high = len(letter)-1
    ans = -1

    while low <= high:

        middle = (low + high)//2

        if letter[middle] <= target:
            low = middle + 1
        else:
            ans = middle
            high = middle - 1
    return letter[ans] if ans != -1 else letter[0]
    




class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        return get_answer_2(letters, target)

        