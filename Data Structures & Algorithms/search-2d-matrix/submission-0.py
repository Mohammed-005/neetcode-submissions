class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:

            row_mid = top + (bottom - top) // 2

            if matrix[row_mid][0] > target:
                bottom = row_mid - 1
            elif matrix[row_mid][-1] < target:
                top = row_mid + 1
            else:
                break

        if top > bottom:
            return False

        low = 0
        high = len(matrix[row_mid]) - 1

        while low <= high:

            mid = low + (high - low) // 2

            if matrix[row_mid][mid] == target:
                return True

            elif matrix[row_mid][mid] < target:
                low = mid + 1
            
            elif matrix[row_mid][mid] > target:
                high = mid - 1

        return False

            