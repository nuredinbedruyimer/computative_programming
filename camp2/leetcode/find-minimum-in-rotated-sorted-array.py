class Solution:
    def findMin(self, nums: List[int]) -> int:
        def get_index(arr):
            low = 0

            high = len(arr)-1

            while low < high:

                middle = (low + high) // 2

                if arr[middle] <= arr[high]:

                    high = middle

                else:

                    low = middle + 1
                    
            return low
        min_index = get_index( nums)
        return nums[min_index]
                    
        