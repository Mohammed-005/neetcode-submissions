from collections import defaultdict


def can_construct(ransomNote: str, magazine: str) -> bool:

    counter = defaultdict(int)

    for char in magazine:
        counter[char] += 1

    for char in ransomNote:

        if char not in counter or counter[char] == 0:
            return False

        else:
            counter[char] -= 1

    return True

print(can_construct("a", "b"))     
print(can_construct("aa", "ab")) 
print(can_construct("aa", "aab"))    
