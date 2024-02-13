class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def get_answer():
            for index,value in enumerate(nums):
                nums[index]=str(value)
            
            def compare_digit(num1,num2):
                if num1+num2>num2+num1:
                    return -1
                else:
                    return 1
            return str(int("".join(sorted(nums,key=cmp_to_key(compare_digit)))))
        return get_answer()