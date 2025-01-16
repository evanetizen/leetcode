class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # first pass
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]

        # second pass
        postfix = 1
        for j in range(len(nums) - 2, -1, -1):
            postfix *= nums[j + 1]
            res[j] = res[j] * postfix

        return res
