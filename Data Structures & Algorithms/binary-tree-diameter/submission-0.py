# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_ht = self.find_ht(root.left)
        right_ht = self.find_ht(root.right)
        via_root = left_ht + right_ht
        via_left = self.diameterOfBinaryTree(root.left)
        via_right = self.diameterOfBinaryTree(root.right)
        return max(via_root, via_left, via_right)

    def find_ht(self, root):
        if root is None:
            return 0
        left_ht = self.find_ht(root.left)
        right_ht = self.find_ht(root.right)
        return 1 + max(left_ht, right_ht)
