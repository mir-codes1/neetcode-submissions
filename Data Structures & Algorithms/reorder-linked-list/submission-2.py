# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # skip, pull last node to front, skip, pull last node to front
        skip = True
        prev = None
        while head.next:
            if skip:
                skip = False
                prev = head
                head = head.next
            else:
                skip = True

                # obtain pointer to last node
                tail = head
                prev_tail = None
                while tail.next:
                    prev_tail = tail
                    tail = tail.next
                
                # bring tail to behind current head
                prev_tail.next = None
                tail.next = head
                prev.next = tail
