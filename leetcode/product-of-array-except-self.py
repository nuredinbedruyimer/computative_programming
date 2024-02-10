class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans=[1]*len(nums)
        # prefix=1
        # for i in range(len(nums)):
        #     ans[i]=prefix
        #     prefix*=nums[i]
        # print(ans)
        # postfix=1
        # for i in range(len(nums)-1,-1,-1):
        #     ans[i]*=postfix
        #     postfix*=nums[i]
        # print(ans)
        # return ans
        def preMul(arr):
            prePro=[1]*(len(arr)+1)
            for i in range(len(arr)):
                prePro[i+1]=prePro[i]*arr[i]
            return prePro
        def postPro(arr):
            postPro=[1]*(len(arr)+1)
            for i in range(len(arr)):
                postPro[i+1]=postPro[i]*arr[len(arr)-i-1]
            return postPro
        def productExceptItSelf(arr):
            post=postPro(arr)
            pre=preMul(arr)
            ans=[1]*len(arr)
            for i in range(len(arr)):
                ans[i]=post[len(arr)-i-1]*pre[i]
            return ans
        return productExceptItSelf(nums)