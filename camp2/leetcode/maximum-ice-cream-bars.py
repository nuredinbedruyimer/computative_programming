class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
    


        # def counting_sort(arr):
        #     size = len(arr)
        #     output = [0] * size

        #     count = [0] * 10

        #     for i in range(0, size):
        #         count[arr[i]] += 1

        #     for i in range(1, 10):
        #         count[i] += count[i - 1]

        #     i = size - 1
        #     while i >= 0:
        #         output[count[arr[i]] - 1] = arr[i]
        #         count[arr[i]] -= 1
        #         i -= 1

        #     for i in range(0, size):
        #         arr[i] = output[i]

        # counting_sort(costs)
        costs.sort()
        total_buy = 0
        pointer = 0
        ans = 0
        while pointer<len(costs) and total_buy<coins:
            total_buy=total_buy+costs[pointer]
            if total_buy<=coins:
                ans+=1
            pointer+=1
        return ans
        