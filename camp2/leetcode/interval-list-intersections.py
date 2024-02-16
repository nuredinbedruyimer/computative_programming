class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        def get_answer():

            first =0
            Nf=len(firstList)
            Ns=len(secondList)
            ans = []
            second = 0 
            while first<Nf and second<Ns:
                # check is there any intersection 
                




                start=max(firstList[first][0], secondList[second][0])
                end=min(firstList[first][1], secondList[second][1])
                # checking intersection
                if start<=end:
                    ans.append([start, end])
                

                if firstList[first][1]<secondList[second][1]:
                    first+=1
                else:
                    second+=1
            return ans
        return get_answer()
                
        