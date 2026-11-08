# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        while list1 and list2:
            smaller = min(list1.val, list2.val)

            if smaller == list1.val:
                head.next = list1
                head = head.next
                list1 = list1.next
            elif smaller == list2.val:
                head.next = list2
                head = head.next
                list2 = list2.next
        
        if not list1:
            head.next = list2
        elif not list2:
            head.next = list1
        return dummy.next