class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairOfSpeedAndPosition=[[pos,spe] for pos,spe in  zip(position,speed)]
        print( pairOfSpeedAndPosition)
        stack=[]
        print(sorted(pairOfSpeedAndPosition[::-1]))
        for pos,spe in  sorted(pairOfSpeedAndPosition)[::-1]:
            stack.append((target-pos)/spe)
            while len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        
        
        
        