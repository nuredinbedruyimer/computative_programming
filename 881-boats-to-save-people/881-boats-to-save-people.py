class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1
        counter=0
        while left<=right:
            space=limit-people[right]
            
            counter=counter+1
            if left<right and space>=people[left]:
                left=left+1
            right=right-1
        return counter
        