class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combSum(index, stack, target, ans, length):
            if target == 0:
                ans.append(stack[:])
                return
            for curr_index in range(index, length):
                if  candidates[curr_index] == candidates[curr_index-1] and curr_index > index :
                    continue
                if candidates[curr_index] > target:
                    break

                stack.append(candidates[curr_index])
                combSum(curr_index + 1 , stack, target - candidates[curr_index], ans, length)
                stack.pop()
        candidates.sort()
        ans=[]
        visited = set()
        stack=[]
        combSum(0,stack,target,ans,len(candidates))
        return ans
            
        