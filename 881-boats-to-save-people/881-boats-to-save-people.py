class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        numberOfBoat=0
        left,right=0,len(people)-1
        while(left<=right):
            remainSpace=limit-people[right]
            right-=1
            numberOfBoat+=1
            
            if left<=right and remainSpace>=people[left]:
                left=left+1
                
            
           
                
        return numberOfBoat