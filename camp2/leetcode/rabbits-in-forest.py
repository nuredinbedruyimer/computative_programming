import math

def get_answer(answers):
        answers.sort()

        current_number = 0

        current_count = 0

        current_sum = 0

        for answer in answers:

            if answer != current_number:
                current_sum += (current_number + 1)*math.ceil(current_count / (current_number + 1))
                current_number = answer
                current_count = 1
            else:
                current_count +=1
        current_sum += (current_number + 1) * math.ceil( current_count /( current_number + 1))
        
        return current_sum




class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        return get_answer(answers)
