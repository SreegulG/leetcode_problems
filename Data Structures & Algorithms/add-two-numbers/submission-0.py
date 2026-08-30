# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        dummy = ListNode(None)
        new_head = dummy
        carry = 0

        while temp1 and temp2:
            s = temp1.val + temp2.val + carry
            digit = s % 10
            carry = s // 10
            new_node = ListNode(digit)
            dummy.next = new_node
            dummy = dummy.next
            temp1 = temp1.next
            temp2 = temp2.next

        while temp1:
            s = temp1.val + carry
            digit = s % 10
            carry = s // 10
            new_node = ListNode(digit)
            dummy.next = new_node
            dummy = dummy.next
            temp1 = temp1.next
        
        while temp2:
            s = temp2.val + carry
            digit = s % 10
            carry = s // 10
            new_node = ListNode(digit)
            dummy.next = new_node
            dummy = dummy.next
            temp2 = temp2.next
        
        if carry:
            new_node = ListNode(carry)
            dummy.next = new_node
        return new_head.next
