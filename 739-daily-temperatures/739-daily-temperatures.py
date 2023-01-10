class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stackOfDayTemp=[]
        for nthDay,temperatureOnNthDay in enumerate(temperatures):
            while stackOfDayTemp and temperatureOnNthDay>stackOfDayTemp[-1][0]:
                stackTemp,stackIndex=stackOfDayTemp.pop()
                ans[stackIndex]=(nthDay-stackIndex)
            stackOfDayTemp.append([temperatureOnNthDay,nthDay])
        return ans
        