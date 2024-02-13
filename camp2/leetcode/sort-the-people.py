class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def get_answer():
            name_height = []
            N = len(names)
            for i in range(N):
                name_height.append((heights[i], names[i]))
            name_height.sort(reverse=True)
            ans = []
            for i in range(N):
                ans.append(name_height[i][1])
            return ans
        return get_answer()
