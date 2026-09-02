# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self._inorder_help(root, ans)
        return ans

    def _inorder_help(self, root, ans):
        if root is None:
            return
        self._inorder_help(root.left, ans)
        ans.append(root.val)
        self._inorder_help(root.right, ans)
