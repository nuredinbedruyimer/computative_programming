class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        def get_two_sum():
            left = 0 
            right = len(arr)-1
            while left<right:
                curr_sum = arr[left]+arr[right] 
                if curr_sum==target:
                    return left+1,right+1

                elif curr_sum>target:
                    right-=1
                else:
                    left+=1
        return get_two_sum()

        