class Solution(object):
    def sumSubarrayMins(self, arr):
        

            
            
        def get_answer():
            stack = []
            min_total = 0
            arr.insert(0, 0)
            arr.append(0) 
            n = len(arr)
            """
            [3,1,2,4]
            3 1 2
            3+1+2+4
            1+1+1
            1+1+2
            17

            """
            ans = [None]*n
            
            for i in range(n):
                while stack and arr[i] < arr[stack[-1]]:
                    mid = stack.pop()
                    left = mid - stack[-1]
                    right = i - mid
                    min_total += left * right * arr[mid]
                    print(min_total)

                stack.append(i)

            return min_total % (10 ** 9 + 7)
        return get_answer()
        