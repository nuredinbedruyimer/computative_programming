class Solution:
    def deckRevealedIncreasing(self, arr: List[int]) -> List[int]:
        def get_answer():
            arr.sort()
            N = len(arr)
            queue = collections.deque([i for i in range(N)])
            index = 0
            memo = [-1 for _ in range(N)]
            while len(queue)>0:
                revealed = queue.popleft()
                memo[revealed] = index
                index+=1
                if len(queue)>0:
                    queue.append(queue.popleft())
            ans = []
            for i in range(N):
                ans.append(arr[memo[i]])
            return ans
        return get_answer()
        


        