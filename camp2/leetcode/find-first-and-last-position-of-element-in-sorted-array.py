# # def get_answer(nums , target):

#     N = len(nums)

#     first_index =  -1


#     for i in range(N):
#         if nums[i] == target:

#             first_index = i

#             break
#     last_index = -1

#     for i in range(N-1, -1, -1):

#         if nums[i] == target:

#             last_index = i
            
#             break
#     return [first_index, last_index]
#  time O(n) space O(1)
def get_left_index(nums , target):

    low = 0

    high = len(nums) - 1

    ans = -1

    while low <= high:

        middle = ( low + high ) // 2

        if nums[middle] == target:

            ans = middle 

            high = middle - 1

        elif nums[middle] > target:

            high=middle - 1

        else:

            low = middle + 1

    return ans
def get_right_index(nums, target):

    low = 0

    high = len(nums) - 1
    ans = -1

    while low <= high:
        middle = ( low + high ) // 2

        if nums[middle] == target:

            ans = middle

            low = middle + 1

        elif  nums[middle] < target:

            low= middle +1
        else:

            high= middle -1

    return ans

def get_answer(nums, target):

    left = get_left_index(nums, target)

    right = get_right_index(nums , target)

    return [left , right]
    


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        return get_answer(nums , target)