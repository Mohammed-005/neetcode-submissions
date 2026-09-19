from collections import defaultdict

def num_jewels_in_stones(jewels: str, stones: str) -> int:

    count = defaultdict(int)
    total_jewels = 0

    for s in stones:
        count[s] += 1

    for ch in jewels:
        total_jewels += count[ch]

    return total_jewels

jewels = "aA"
stones = "aAAbbbb"

print(num_jewels_in_stones(jewels, stones))
