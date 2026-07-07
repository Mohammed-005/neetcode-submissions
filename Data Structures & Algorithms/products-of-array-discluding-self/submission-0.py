class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums)
        result = [0] * len(nums)

        left_total = 1
        right_total = 1

        for i in range(len(nums)):
            left_arr[i] = left_total
            left_total *= nums[i]

        for i in reversed(range(len(nums))):
            right_arr[i] = right_total
            right_total *= nums[i]
        
        for i in range(len(nums)):
            result[i] = left_arr[i] * right_arr[i]

        return result