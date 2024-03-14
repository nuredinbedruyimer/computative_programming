class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def get_answer():

            distance = []

            for i in range(len(arr)):
                #  finding distance of the every element from the point X

                D = abs(arr[i] - x)


                distance.append((D, i))


            heapify(distance)

            ans = []

            for i in range(k):
                
                ans.append(heapq.heappop(distance)[1])
            
            ans.sort()

            temp = []
            

            for i in ans:

                temp.append( arr[i])

            return temp

        return get_answer()
