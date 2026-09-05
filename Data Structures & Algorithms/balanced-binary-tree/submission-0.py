# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.find_ht(root)[1]

    def find_ht(self, root):
        if root is None:
            return 0, True
        left_ht, left_balanced = self.find_ht(root.left)
        right_ht, right_balanced = self.find_ht(root.right)
        ht = 1 + max(left_ht, right_ht)
        balanced = left_balanced and right_balanced and abs(left_ht - right_ht) <= 1
        return ht, balanced
