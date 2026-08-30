"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None
        node_map = {}
        temp = head

        while temp:
            new_node = Node(temp.val)
            node_map[temp] = new_node
            temp = temp.next
        temp = head
        while temp:
            curr = node_map[temp]
            curr.next = node_map.get(temp.next)
            curr.random = node_map.get(temp.random)
            temp = temp.next
        return node_map[head]
