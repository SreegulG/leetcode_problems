# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.find_ht(root)
        return self.ans

    def find_ht(self, root):
        if root is None:
            return 0
        left_ht = self.find_ht(root.left)
        right_ht = self.find_ht(root.right)
        self.ans = max(self.ans, left_ht + right_ht)
        return 1 + max(left_ht, right_ht)
