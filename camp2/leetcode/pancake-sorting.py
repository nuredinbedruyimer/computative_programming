class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def get_index(value, arr):
            memo = {}
            for i in range(len(arr)):
                memo[arr[i]] = i
            return memo[value]
        def get_answer():
            N=len(arr)
            ans=[]
            for i in range(N):
                max_value=max(arr[:N-i])
                max_index=get_index(max_value, arr)+1
                arr[:max_index]=reversed(arr[:max_index])
                ans.append(max_index)
                arr[:N-i]=reversed(arr[:N-i])
                ans.append(N-i)
            return ans
        return get_answer()
        
       