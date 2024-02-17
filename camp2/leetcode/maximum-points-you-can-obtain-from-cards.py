class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        """
        k = 3
        [1,2,3,4,5,6,1]
             [_ _ _ _]-->10
        min_sum= 10
        min_sum = 14
        min_sum = 18
        min_of all of the above is 10
        then my remaining sum is surly my max_score
        in this case  total-min_sum ==22-10==12


        using the scanner like window we can check for min sum by adding one from left and renove other
        element from the other end
        
        """
        def get_answer():
            N = len(arr)
            total = 0
            for  i in range(N-k):
                total =total+arr[i]
            min_sum = total
            left = 0
            for i in range(N-k, N):
                total-=arr[left]
                total+=arr[i]
                left+=1
                min_sum = min(min_sum, total)
            return sum(arr)-min_sum
        return get_answer()


        