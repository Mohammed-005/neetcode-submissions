from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s = defaultdict(int)

        for ch in s:
            count_s[ch] += 1

        for ch in t:
            if ch not in count_s or count_s[ch] == 0:
                return False
            else:
                count_s[ch] -= 1

        return True        