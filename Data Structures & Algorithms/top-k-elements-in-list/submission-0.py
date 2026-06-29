class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, freq_count in count.items():
            freq[freq_count].append(num)

        result = []

        for bucket in reversed(freq):

            for num in bucket:
                result.append(num)

                if len(result) == k:
                      return result

        return result