def word_pattern(pattern: str, s: str) -> bool:

    words = s.split(' ')

    if len(words) != len(pattern):
        return False

    map_pattern_to_s = {}
    map_s_to_pattern = {}

    for i in range(len(words)):
        char_pattern = pattern[i]
        char_s = words[i]

        if char_pattern in map_pattern_to_s:
            if map_pattern_to_s[char_pattern] != char_s:
                return False

        if char_s in map_s_to_pattern:
            if map_s_to_pattern[char_s] != char_pattern:
                return False

        map_pattern_to_s[char_pattern] = char_s
        map_s_to_pattern[char_s] = char_pattern

    return True

print(word_pattern("abba", "dog cat cat dog"))  
print(word_pattern("abba", "dog cat cat fish"))
print(word_pattern("aaaa", "dog cat cat dog"))   
