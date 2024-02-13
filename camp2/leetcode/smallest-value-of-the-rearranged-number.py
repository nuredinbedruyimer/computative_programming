class Solution:
    def smallestNumber(self, num: int) -> int:
        def get_rearranged_number(number):
            arr = list(str(number))
            if number>=0:
                arr.sort()
                left = 0
                if number == 0:
                    return 0
                while left < len(arr) and arr[left]=='0':
                    left+=1
                print(left)
                arr[0], arr[left] = arr[left], arr[0]
                return int("".join(arr))
            else:
                arr.pop(0)
                arr.sort(reverse=True)
                return -1*int("".join(arr))
                
            
                
        def get_answer():
            return get_rearranged_number(num)
        return get_answer()

        """
        positive sort in acc order ans swap any leading zero with other element

        negative sort in desc order ans return that
        
        """
        