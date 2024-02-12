class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_answer():
            nums1.sort()
            nums2.sort()
            N1 = len(nums1)
            N2 = len(nums2)
            left = 0
            right = 0
            ans = []
            while left<N1 and right<N2:
                if nums1[left]==nums2[right]:
                    ans.append(nums1[left])
                    left+=1
                    right+=1
                elif nums1[left]>nums2[right]:
                    right+=1
                elif nums2[right]>nums1[left]:
                    left+=1
            return ans
        return get_answer()
            
        