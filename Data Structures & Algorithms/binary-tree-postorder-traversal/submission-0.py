# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self._postorder_helper(root, ans)
        return ans

    def _postorder_helper(self, root, ans):
        if root is None:
            return
        self._postorder_helper(root.left, ans)
        self._postorder_helper(root.right, ans)
        ans.append(root.val)
