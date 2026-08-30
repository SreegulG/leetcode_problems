"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        temp = head

        while temp:
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next
        
        temp = head
        while temp:
            new_node = temp.next
            if temp.random:
                new_node.random = temp.random.next
            temp = new_node.next

        new_head = head.next
        temp = head
        while temp:
            new_node = temp.next
            temp.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            temp = temp.next
        return new_head