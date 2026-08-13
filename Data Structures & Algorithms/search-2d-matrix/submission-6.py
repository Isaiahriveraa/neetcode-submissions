class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        for row in range(m):
            for col in range(n):

                if matrix[row][0] <= target <= matrix[row][n - 1]:

                    # search using binary search
                    left, right = 0, n - 1

                    while left <= right:
                        mid = (left + right) // 2

                        if matrix[row][mid] == target:
                            return True
                        elif matrix[row][mid] < target:
                            left = mid + 1
                        else:
                            right = mid - 1
        return False