class Solution:
    """
    A class containing a method to count the number of negative numbers
    in a sorted 2D grid (sorted in non-increasing order both row-wise and column-wise).
    """

    def countNegatives(self, grid):
        """
        Count the total number of negative numbers in a 2D grid.

        Parameters
        ----------
        grid : List[List[int]]
            A 2D list of integers where each row and column is sorted in non-increasing order.

        Returns
        -------
        int
            The count of negative numbers in the grid.
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        row = rows - 1  # Start from the bottom-left corner
        col = 0  # Start from the first column
        while row >= 0 and col < cols:
            if grid[row][col] < 0:
                # All elements in the current row from 'col' to end are negative
                count += cols - col
                row -= 1  # Move one row up to continue checking
            else:
                col += 1  # Move right in the current row
        return count


sol = Solution()
grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]
]
print(sol.countNegatives(grid))
