class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        [1,5,10]
        
        
        """
        def generate_number(curr_value, max_value, counter):
            while curr_value>max_value+1:
                max_value+=max_value+1
                counter+=1
                if max_value>=n:
                    break
            return (max_value, counter)
                


        def get_answer():
            N= len(nums)
            max_value = 0
            patches = 0
            for i in range(N):


                """
                [1]--> 1 when i add 2 to one i am able to generate 1 2 3 
                [1, 2]--->1 2 3  when  i add  1+2 or 3 to the element i am able 
                to generate  1 2 3
                             3 3 3
                             4 5 6
                [1, 2, 3] ---> 1 2 3 4 5 6
                what about adding 4   we have like   1 2 3 4 5 6 
                                                     

                example [1 5 10]
                [1]-->1
                adding [1, 2]--->1 2 3
                adding 3 [1, 2, 3]---> 1, 2, 3, 4,5,6 
                                  
                adding 5 [1, 2, 3, 5]--> 1 2 3 4 5 6
                                         5 5 5 5 5 5
                                         1 2 3 4 5 6 --Intial
                                         6 7 8 9 10 11 added due to 5
                untill now we have 1   2  3  4  5  6  7  8  9  10  11  when we use 10
                let 10->1          10  10 10 10 10 10 10 10 10 10  10
                               then by using [1, 2,3, 5,10]--> we can generate untill
                                21 then ans will be 2 because we just add 2 element
                                
                
                
                """
                if nums[i]>max_value+1:
                    max_value, patches = generate_number(nums[i], max_value, patches)
                max_value+=nums[i]
                if max_value>=n:
                    break
            while max_value<n:
                max_value+= max_value+1
                patches+=1
            return patches
        return get_answer()



        