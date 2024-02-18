class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        
        [1, 3] distance= 3**2 + 1**2 = 10
        [-2, 2] distance = (-2)**2 + 2**2 = 8
        answer= [8, 10]
        first closest = 8
        second closest = 10
        use distance with index to heap or to be more friendly with our topic we can use sorting
       


       TO COMPARE HEAP AND THAT OF SORTED SOLUTION 
       HEAP---> NLOG(K)---> FASTER IN MOST CASE
       SORTING --->NLOG(N) -----
       IN THE WEREST CASE BOTH BECOME NLOG(N)----> 









        
        """
        # def get_answer_one():
        #     _heap = []
        #     heapq.heapify(_heap)
        #     for i in range(len(points)):
        #         distance = points[i][0]**2 + points[i][1]**2
        #         heapq.heappush(_heap, (distance, i))
        #     index = 0
        #     ans = []
        #     for i in range(k):
        #         d, index = heapq.heappop(_heap)
        #         ans.append(points[index])
        #     return ans
        # return get_answer_one()
        def get_answer():
            arr = []
            N = len(points)
            for i in range(N):
                distance = points[i][0]**2 + points[i][1]**2
                arr.append((distance, i))
            arr.sort()
            ans = []
            for i in range(k):
                ans.append(points[arr[i][1]])
            return ans
        return get_answer()


        


        