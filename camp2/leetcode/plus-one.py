class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def get_answer():
            number= ""
            for i in digits:
                number+=str(i)
            number = str(int(number)+1)
            ans = []
            for i in range(len(number)):
                ans.append(int(number[i]))
            return ans
        return get_answer()
        