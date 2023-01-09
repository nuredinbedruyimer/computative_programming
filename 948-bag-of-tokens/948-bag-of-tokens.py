class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        que=deque(sorted(tokens))
        score=0
        minScore=0
        while que:
            if power>=que[0]:
                t=que.popleft()
                power=power-t
                score=score+1
                minScore=max(score, minScore)
            elif score>0:
                t=que.pop()
                power=power+t
                score=score-1
            else:
                break
        return minScore
        