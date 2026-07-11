class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)
        best_speed = 0

        while low <= high:

            mid = low + (high - low) // 2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)

            if total_time <= h:
                best_speed = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return best_speed
        