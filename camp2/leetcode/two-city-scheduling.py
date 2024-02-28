def get_answer(costs):
    sorted_costs = sorted(costs, key=lambda x : x[0]-x[1])
    # print(sorted_costs)



    N = len(costs)
    
    
    cost_for_city_a = 0

    for i in range(N//2):

        cost_for_city_a +=sorted_costs[i][0] 
    
    cost_for_city_b = 0


    for i in range(N//2, N):

        cost_for_city_b +=sorted_costs[i][1] 
    
    return (cost_for_city_a + cost_for_city_b)



class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return get_answer(costs)
        

        