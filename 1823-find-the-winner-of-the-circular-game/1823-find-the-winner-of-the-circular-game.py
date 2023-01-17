class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def getIndex(currentIndex,step,length):
            nextIndex=currentIndex+step-1
            if nextIndex>=length:
                nextIndex%=length
            return nextIndex
        def ans(arr,index):
            length=len(arr)
            if length==1:
                return arr[0]
            else:
                arr.pop(index)
                return ans(arr,getIndex(index,k,length-1))
        return ans([i for i in range(1,n+1)],getIndex(0,k,n))
        