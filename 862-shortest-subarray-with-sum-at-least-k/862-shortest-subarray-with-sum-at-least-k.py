class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        length=len(nums)
        total=[0]
        for i in range(length):
            total.append(nums[i]+total[-1])
        increasingQueue=deque()
        subArrayLength=sys.maxsize
        for right,value in enumerate(total):
            while increasingQueue and value-total[increasingQueue[0]]>=k:
                subArrayLength=min((right-increasingQueue.popleft()),subArrayLength)
            while increasingQueue and value<=total[increasingQueue[-1]]:
                increasingQueue.pop()
            increasingQueue.append(right)
        if subArrayLength < sys.maxsize :
            return subArrayLength
        else:
            return -1       
                
                
                
        