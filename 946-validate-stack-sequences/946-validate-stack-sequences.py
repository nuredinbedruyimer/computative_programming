class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        right=len(popped)
        left=0
        for element in pushed:
            stack.append(element)
            while stack and left<right and stack[-1]==popped[left]:
                left+=1
                stack.pop()
        return stack==[]
        