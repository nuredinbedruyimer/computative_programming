class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        def reverse(arr):
            left = 0
            right = len(arr)-1
            while left<=right:
                arr[right], arr[left] = arr[left], arr[right]
                left+=1
                right-=1
            return arr
        def flip(arr):
            for i  in range(len(arr)):
                if arr[i]:
                    arr[i]=0
                else:
                    arr[i]=1
            return arr
        ans = []
        def get_answer(image):
            for row in range(n):
                data = reverse(image[row])
                reverse_row = flip(data)
                ans.append(reverse_row)
            return ans
        return get_answer(image)

        