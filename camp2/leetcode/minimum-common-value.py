class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def get_answer():
            left = 0
            right = 0
            N1=len(nums1)
            N2 = len(nums2)
            
            while right<N2 and left<N1:

                if nums1[left]==nums2[right]:
                    return nums1[left]
                elif nums1[left]>nums2[right]:
                    right+=1
                else:
                    left+=1
            return -1
        return get_answer()

        