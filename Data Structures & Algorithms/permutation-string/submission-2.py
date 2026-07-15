from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        s1_count = defaultdict(int)
        window_count = defaultdict(int)

        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):

            s1_count[s1[i]] += 1

        for i in range(k):

            window_count[s2[i]] += 1

        if window_count == s1_count:
            return True

        for i in range(k, len(s2)):

            window_count[s2[i]] += 1
            window_count[s2[i - k]] -= 1

            if window_count[s2[i - k]] == 0:
                del window_count[s2[i-k]]

            if window_count == s1_count:
                return True

        return False