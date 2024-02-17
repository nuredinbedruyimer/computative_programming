class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        def get_answer():
            memo = {}
            N =len(cards)


            min_length=N+1
            for right , card in enumerate(cards):
                if card in memo:
                    min_length = min(min_length, right-memo[card] + 1)
                memo[card] = right

            if min_length == N+1:
                return -1
                
            else:
                return  min_length
        return  get_answer()
        