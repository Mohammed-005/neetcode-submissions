class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        left = 0

        for right in range(len(nums)):

            if nums[right] in seen:
                return True

            seen.add(nums[right])

        return False