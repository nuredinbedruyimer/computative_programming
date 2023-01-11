class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index,value in enumerate(nums):
            nums[index]=str(value)
            
        def compareDigit(num1,num2):
            if num1+num2>num2+num1:
                return -1
            else:
                return 1
        result=sorted(nums,key=cmp_to_key(compareDigit))
        return str(int("".join(result)))