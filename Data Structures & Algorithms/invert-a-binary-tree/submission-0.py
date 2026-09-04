# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert_tree_helper(root)
        return root

    def invert_tree_helper(self, root):
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invert_tree_helper(root.left)
        self.invert_tree_helper(root.right)
