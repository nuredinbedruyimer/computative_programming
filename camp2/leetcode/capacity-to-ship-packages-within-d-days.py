def black_box(weight , weights, days):

    curr_weight = 0

    curr_days = 1


    for w in weights:


        curr_weight += w

        if curr_weight > weight:

            curr_weight = w

            curr_days += 1
        
        

    return curr_days <= days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)
        
        high = sum(weights)

        ans = high +1

                
        while low <= high:

            middle = ( low + high ) // 2

            if black_box( middle , weights, days ):

                ans = min(ans, middle)

                high  = middle - 1
                
                
            else:

                low = middle + 1
                
        return ans
        