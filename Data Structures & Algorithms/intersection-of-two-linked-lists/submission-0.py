# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB

        while temp1:
            while temp2:
                if temp1 == temp2:
                    return temp1
                temp2 = temp2.next
            temp2 = headB
            temp1 = temp1.next