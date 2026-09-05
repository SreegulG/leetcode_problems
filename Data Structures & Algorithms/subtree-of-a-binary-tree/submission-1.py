# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        is_left_same = self.is_same_tree(p.left, q.left)
        is_right_same = self.is_same_tree(p.right, q.right)
        return is_left_same and is_right_same
