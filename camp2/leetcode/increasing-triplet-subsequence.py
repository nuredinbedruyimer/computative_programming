class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #  because we need increasing subsequence then we can use monotonic stack
        #  check when ever the stack become >=3 return true else return false
        #  generate all max element  and min on our stack
        def get_answer():
            N = len(nums)
            min_stack = []
            for i in range(N):
                if min_stack and nums[i]>min_stack[-1]:
                    min_stack.append(min_stack[-1])
                else:
                    min_stack.append(nums[i])
            max_stack = []
            for i in range(N-1, -1, -1):
                if max_stack and nums[i]<max_stack[-1]:
                    max_stack.append(max_stack[-1])
                else:
                    max_stack.append(nums[i])
            max_stack = max_stack[::-1]
            for i in range(N-1):
                if min_stack[i]<nums[i]<max_stack[i]:
                    return True
            return False

            
                
        return get_answer()



        