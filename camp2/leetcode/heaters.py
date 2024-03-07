class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
               L
        [1, 2, 3, 4, 8, 29]
            R
        [1, 8, 19, 25]
        first we fing heating at 1 and find the distance 0
        find 8 and 2 and 1 and two then we take 1

        
        """
        
        heaters = [-10**9] + heaters + [2*10**9+7]
        
        ans = 0

        houses.sort()

        # handle edge case by adding extrame vlue on the both end of heater
        heaters.sort()

        start = 1

        for house in houses:

            while heaters[start]<house:

                start+=1

            temp = min(house-heaters[start - 1], heaters[start] - house) 

            ans = max(ans, temp)

        return  ans


        