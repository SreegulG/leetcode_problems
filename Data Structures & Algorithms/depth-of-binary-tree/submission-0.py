# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth_helper(root)

    def max_depth_helper(self, root):
        if root is None:
            return 0

        left_ht = self.max_depth_helper(root.left)
        right_ht = self.max_depth_helper(root.right)

        return 1 + max(left_ht, right_ht)
