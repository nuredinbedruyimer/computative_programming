class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def get_answer():
            N=len(strs)
            M= len(strs[0])
            arr = []
            for column in range(M):
                temp =""
                for row in range(N):
                    temp=temp+strs[row][column]
                arr.append(temp)
            print(arr)
            
            ans = 0
            for i in arr:
                if list(i)!=sorted(i):
                    ans+=1
            return ans
        return get_answer()
        