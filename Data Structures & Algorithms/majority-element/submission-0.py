from collections import defaultdict

def majority_element(nums: list[int]) -> int:

    target = len(nums) // 2

    counter = defaultdict(int)

    for num in nums:
        counter[num] += 1

    for num, count in counter.items():
        if count > target:
            return num

    return -1

nums = [3, 2, 1]
print(majority_element(nums))
