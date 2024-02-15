class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def get_answer():
            for index,value in enumerate(nums):
                nums[index]=str(value)
            
            def compare_digit(num_one,num_two):
                # comparing  34 and othe like 31  3+4>3+1
                if num_one+num_two>num_two+num_one:
                    return -1
                else:
                    return 1
            return str(int("".join(sorted(nums,key=cmp_to_key(compare_digit)))))
        return get_answer()