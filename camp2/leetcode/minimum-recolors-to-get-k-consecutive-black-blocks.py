class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        def get_answer():
            N = len(blocks)
            white = 0
            for i in range(k):
                if blocks[i]=='W':
                    white+=1
            min_opt =white
            for i in range(k,N):
                white+= blocks[i]=='W'
                white-= blocks[i-k]=='W'
                min_opt = min(min_opt, white)
            return min_opt
        return get_answer()

        