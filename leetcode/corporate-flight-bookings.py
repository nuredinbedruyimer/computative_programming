class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        def get_answer():
            N=n+1
            marking = [0 for _ in range(N)]
            for first, last, seat in bookings:
                marking[first-1]+=seat
                marking[last] -= seat
            prefix_sum=[marking[0]]
            for i in range(1,n):
                prefix_sum.append(prefix_sum[-1]+marking[i])
            return prefix_sum
        return get_answer()



        