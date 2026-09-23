class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1 for i in range(len(nums))]

        i = 0
        while i < len(nums) - 1:
            temp[i+1] *= temp[i] * nums[i]
            i += 1

        i = len(nums) - 1
        postfix = 1
        while i > 0:
            postfix *= nums[i] 
            temp[i - 1] = temp[i - 1] * postfix
            i -= 1
            
        return temp
