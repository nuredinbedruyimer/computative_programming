class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newStones=[-i for i in stones]
        heapq.heapify(newStones)
        while(len(newStones)>1):
            one=heapq.heappop(newStones)
            two=heapq.heappop(newStones)
            heapq.heappush(newStones,one-two)
        return abs(newStones[0])