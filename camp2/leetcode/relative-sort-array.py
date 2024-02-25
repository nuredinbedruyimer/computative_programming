class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def get_answer():
            N1= len(arr1)
            N2= len(arr2)
            memo={}
            for i in arr1:
                if i in memo:
                    memo[i]+=1
                else:
                    memo[i]=1
            seen = set(arr2)
            ans = []
            temp = []
            for i in arr2:
                if i in seen:
                    ans.extend([i]*memo[i])
            for i in arr1:
                if i not in seen:
                    temp.append(i)
                
            return ans + sorted(temp)
            
        return get_answer()