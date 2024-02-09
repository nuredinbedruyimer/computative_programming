class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def get_answer():
            marking = [0 for _ in range(1005)]
            for passenger, start, end  in trips:
                marking[start+1]+=passenger
                marking[end+1]-=passenger
            prefix_sum=[marking[0]]
            for i in range(1,len(marking)):
                prefix_sum.append(prefix_sum[-1]+marking[i])  
            max_capacity_get_so_far = max(prefix_sum)
            if max_capacity_get_so_far<=capacity:
                return True
            else:
                return False
        return get_answer()
        