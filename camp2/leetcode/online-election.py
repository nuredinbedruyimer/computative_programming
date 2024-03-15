class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leader = []
        votes = defaultdict(int)
        winner = -1
        for person in persons:
            votes[person] += 1
            if votes[person] >= votes[winner]:
                winner = person
            self.leader.append(winner)

    def q(self, t: int) -> int:
        ans = -1
        low, high = 0, len(self.times)
        while low <high:
            
            middle = low + (high - low) // 2
            if t < self.times[middle]:
                high = middle 
            else:
                low = middle + 1
        return self.leader[low - 1]
