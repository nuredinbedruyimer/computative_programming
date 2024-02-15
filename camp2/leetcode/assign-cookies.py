class Solution:
    def findContentChildren(self, greed: List[int], sizes: List[int]) -> int:
        def get_answer():
            greed.sort()
            sizes.sort()
            Ng = len(greed)
            Ns = len(sizes)
            greed_pointer = 0
            sizes_pointer = 0
            content_children =0
            while greed_pointer<Ng and sizes_pointer<Ns:
                if sizes[sizes_pointer]>=greed[greed_pointer]:
                    content_children+=1
                    greed_pointer+=1
                    sizes_pointer+=1
                else:
                    sizes_pointer+=1
            return content_children
        return get_answer()



        