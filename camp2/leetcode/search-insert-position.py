# def get_answer(arr, target):
#     N = len(arr)
#     for i in range(N):
#         if arr[i] == target:
#             return i
#         elif arr[i] > target:
#             return i
#     return N


def get_answer(arr, target):

    low = 0

    high = len(arr) - 1

    while low <= high :

        middle =  (high+low)//2

        if arr[middle] == target:
            return middle

        elif arr[middle] < target:

            low = middle + 1
        else:
            high =  middle - 1
    return low

            



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #  have O(n) using linear search with O(1) space complity
        #  using binary search we can do in log(n ) with O(1) time complity
        return get_answer(nums, target)