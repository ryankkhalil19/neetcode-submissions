class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1
        while top <= bottom:
            middle = (top + bottom) // 2
            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break

        if top > bottom:
            return False

        row = (bottom + top) // 2
        left = 0
        right = COLS - 1
        while left <= right:
            m = (left + right) // 2
            if target < matrix[row][m]:
                right = m - 1
            elif target > matrix[row][m]:
                left = m + 1
            else:
                return True
        return False
