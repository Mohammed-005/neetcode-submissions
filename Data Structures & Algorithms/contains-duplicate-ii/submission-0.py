def contains_nearby_duplicate(nums: list[int], target: int) -> bool:

    seen = {}

    for i in range(len(nums)):

        if nums[i] not in seen:
            seen[nums[i]] = i
        else:
            length = i - seen[nums[i]]

            if length <= target:
                return True

            seen[nums[i]] = i

    return False

print(contains_nearby_duplicate([1, 2, 3, 1], 3))     
print(contains_nearby_duplicate([1, 0, 1, 1], 1))      
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
