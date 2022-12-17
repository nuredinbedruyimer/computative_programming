import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        collector=[]
        for i in range(len(matrix)):
            collector.extend(matrix[i])
        collector.sort()
        print(collector)
        return collector[(k-1)]
            
        