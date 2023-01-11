class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        ans=[intervals[0]]
        for currentStart,currentEnd in intervals[1:]:
            lastEnd=ans[-1][1]
            if currentStart <=lastEnd:
                ans[-1][1]=max(currentEnd,lastEnd)
            else:
                ans.append([currentStart,currentEnd]) 
        return ans
            
        
        