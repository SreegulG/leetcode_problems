# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.find_ht(root) != -1

    def find_ht(self, root):
        if root is None:
            return 0
        left_ht = self.find_ht(root.left)
        if left_ht == -1:
            return -1
        right_ht = self.find_ht(root.right)
        if right_ht == -1:
            return -1

        if abs(left_ht - right_ht) > 1:
            return -1
        ht = 1 + max(left_ht, right_ht)
        return ht
