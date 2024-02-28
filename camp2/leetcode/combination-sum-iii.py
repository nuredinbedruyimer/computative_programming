class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        def get_sum(arr):
            total = 0
            for i in arr:
                total+=i
            return total
        high = 9
        def comb_sum(ind, target, k, stack, ans):
            if len(stack) == k and get_sum(stack) == target:
                ans.append(stack[:])
                return
            for i in range(ind, high+1):
                stack.append(i)
                comb_sum(i+1, target, k, stack, ans)
                stack.pop()
                
        ans = []
        comb_sum(1, target, k, [], ans)
        return ans