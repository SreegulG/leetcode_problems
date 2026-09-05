# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = Queue()
        q.put(root)
        ans = []
        while not q.empty():
            level = []
            n = q.qsize()
            for _ in range(n):
                node = q.get()
                if node:
                    level.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            if level:
                ans.append(level)
        return ans
