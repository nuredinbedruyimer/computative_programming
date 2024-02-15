class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        def get_answer():
            people.sort()
            left = 0
            right = len(people)-1
            boat = 0
            while left<=right:
                curr_load = people[right]+people[left]
                if curr_load<=limit:
                    boat+=1
                    right-=1
                    left+=1
                else:
                    boat+=1
                    right-=1
            return boat
        return get_answer()


        