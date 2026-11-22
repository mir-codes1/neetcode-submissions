# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find nth node
        length = 1
        i = head
        while i.next:
            length += 1
            i = i.next
        
        target_i = length-n
        curr, prev, i = 0, None, head

        while i:
            if curr == target_i:
                # current node is target
                if prev:
                    prev.next = i.next
                else:
                    return head.next

            curr += 1
            prev = i
            i = i.next
        return head