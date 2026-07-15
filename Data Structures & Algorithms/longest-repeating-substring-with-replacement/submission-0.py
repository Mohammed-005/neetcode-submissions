from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        result = 0
        counts = defaultdict(int)

        for right in range(len(s)):

            counts[s[right]] += 1

            while (right - left + 1) - max(counts.values()) > k:

                counts[s[left]] -= 1

                left += 1

            result = max(result, right - left + 1)

        return result
        