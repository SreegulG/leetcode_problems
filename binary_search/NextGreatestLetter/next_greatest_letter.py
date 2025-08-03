class Solution:
    """
    A class containing a method to find the smallest letter greater than the target
    in a sorted list of letters that wraps around cyclically.
    """

    def nextGreatestLetter(self, letters, target):
        """
        Find the smallest letter in the list that is greater than the target.
        The list `letters` is assumed to be sorted and wraps around cyclically,
        meaning if no letter is greater than the target, return the first letter.

        Parameters
        ----------
        letters : list of str
            A sorted list of lowercase letters (e.g., ['c', 'f', 'j']).
        target : str
            A target lowercase letter.

        Returns
        -------
        str
            The smallest letter in `letters` that is lexicographically greater than `target`.
            If such letter does not exist (target is greater or equal to last letter),
            returns the first letter in the list (wrap-around behavior).
        """
        start = 0
        end = len(letters) - 1
        if letters[-1] <= target:
            return letters[0]
        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return letters[start]


# Example usage
sol = Solution()
letters1 = ["c", "f", "j"]
print(sol.nextGreatestLetter(letters1, "j"))
