class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method one chearing
        # def get_answer_1():
        #     nums.sort()
        # get_answer_1()
        # Method two counting
        # def get_answer_2():
        #     zero = 0
        #     one = 0
        #     two = 0 
        #     for n in nums:
        #         if n==0:
        #             zero+=1
        #         elif n==1:
        #             one+=1
        #         else:
        #             two+=1
            
        #     for i in range(zero):
        #         nums[i] =0
                
        #     for i in range(zero, zero+one):
        #         nums[i]=1
        #     for i in range(zero+one, one+zero+two):
        #         nums[i] = 2
        # get_answer_2()
        # method 3 using detch flag algorithm
        #  left right and middle pointer
        def get_answer_3():
            left =middle = 0
            right = len(nums)-1
            while middle<=right:
                if nums[middle]==0:
                    nums[left], nums[middle] = nums[middle], nums[left]
                    left+=1
                    middle+=1
                elif nums[middle]==2:
                    nums[right], nums[middle] = nums[middle], nums[right]
                    right-=1
                else:
                    middle+=1
        get_answer_3()
            


        