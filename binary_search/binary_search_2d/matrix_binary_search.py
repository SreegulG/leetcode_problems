class Solution:
    """
    A class to perform efficient search in a 2D matrix where each row is sorted
    and the first integer of each row is greater than the last integer of the previous row.
    """

    def searchMatrix(self, matrix, target):
        """
        Search for a target value in a 2D matrix using binary search.

        The matrix is treated as a flattened sorted array by calculating the row
        and column indices based on the middle index.

        Parameters
        ----------
        matrix : List[List[int]]
            A 2D list of integers sorted as specified above.
        target : int
            The integer value to search for.

        Returns
        -------
        bool
            True if target is found in the matrix, False otherwise.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows * cols - 1
        while start <= end:
            mid = start + (end - start) // 2
            row = mid // cols  # Map mid to row index
            col = mid % cols  # Map mid to column index
            if matrix[row][col] > target:
                end = mid - 1  # Search left half
            elif matrix[row][col] < target:
                start = mid + 1  # Search right half
            else:
                return True  # Target found
        return False  # Target not found


mat = [[1, 3]]
sol = Solution()
print(sol.searchMatrix(mat, 3))
