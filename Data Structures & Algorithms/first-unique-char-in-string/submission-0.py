from collections import defaultdict

def first_unique_char(s: str) -> int:

    counter = defaultdict(int)

    for ch in s:
        counter[ch] += 1

    for i in range(len(s)):
        current_char = s[i]

        if counter[current_char] == 1:
            return i

    return -1

s = 'aabb'
print(first_unique_char(s))
