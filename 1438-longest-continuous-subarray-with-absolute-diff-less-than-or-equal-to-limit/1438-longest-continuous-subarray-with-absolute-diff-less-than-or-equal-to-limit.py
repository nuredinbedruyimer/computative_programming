class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decreasingDeque=deque()
        increasingDeque=deque()
        ans=0
        leftPointer=0
        for rightPointer,value in enumerate(nums):
            while decreasingDeque and value>decreasingDeque[-1]:
                decreasingDeque.pop()
            decreasingDeque.append(value)
            while increasingDeque and value<increasingDeque[-1]:
                increasingDeque.pop()
            increasingDeque.append(value)
            while decreasingDeque[0]-increasingDeque[0]>limit:
                if decreasingDeque [0]==nums[leftPointer]:
                    decreasingDeque.popleft()
                if increasingDeque[0]==nums[leftPointer]:
                    increasingDeque.popleft()
                leftPointer+=1
            ans=max(ans,rightPointer-leftPointer+1)
        return ans
                
        