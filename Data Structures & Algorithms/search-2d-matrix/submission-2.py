class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        for row in range(m):
            if matrix[row][0] <= target <= matrix[row][n - 1]: # target is guaranteed to be in here other wise we just return False  
                l, r = 0, n - 1

                while l <= r:
                    mid = (l + r) // 2

                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        # go left
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            
        return False