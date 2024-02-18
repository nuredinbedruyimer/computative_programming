class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:


        """
        
                  i

        [0,3,2,1]
              i

        
        """
        def get_answer():
            N = len(arr)
            if N<3:
                return False
            left = 0
            # we have to find only one peack element not more than one
            # finding increasing part there may be two case have no increasing part or increase all the time 
            #  in thatcase i shod return False    all increasing by it self and deaxreasing arr not valid 
            while left<N-1 and arr[left]<arr[left+1]:
                left+=1
            if left==0 or left==N-1:
                return False
            right = left
            while right<N-1 and arr[right]>arr[right+1]:
                right+=1
            # the next part should be move untill by keeping same monotonocity

            return right==N-1
        return get_answer()
        