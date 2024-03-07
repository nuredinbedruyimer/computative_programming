from  bisect  import bisect_left , bisect_right


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
        
        

        ans = 0

        


        # handle edge case by adding extrame vlue on the both end of heater
        heaters.sort()

        N = len(heaters)

        start = 1

        for house in houses:

            #  finding heater value that have larger value but the smallest one
            #  to do that we use bisect_left in order to find the smallest greater
            #  element

            # should less than the length of arr
            heater_index = bisect_left(heaters , house)

            
            min_radius = float('inf')

            if heater_index < N:
                
                min_radius = min(min_radius , abs(house - heaters[heater_index]))
            

            if heater_index > 0:
                min_radius = min(min_radius , abs(heaters[heater_index - 1 ] - house))

            ans = max(min_radius, ans)


            

            

            

        return  ans


         