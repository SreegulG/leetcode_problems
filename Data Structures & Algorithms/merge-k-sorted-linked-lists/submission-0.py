# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i < len(lists) - 1 else None
                merge_node = self.merge(l1, l2)
                merged_list.append(merge_node)
            lists = merged_list
        return lists[0]

    def merge(self, h1, h2):
        dummy = ListNode(0)
        new_head = dummy
        while h1 and h2:
            if h1.val > h2.val:
                dummy.next = h2
                h2 = h2.next
            else:
                dummy.next = h1
                h1 = h1.next
            dummy = dummy.next

        if h1:
            dummy.next = h1
        if h2:
            dummy.next = h2
        return new_head.next
