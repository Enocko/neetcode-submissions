# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        s1, s2 = head, prev
        while s2:
            s1_val, s2_val = s1.next, s2.next
            s1.next = s2
            s2.next = s1_val
            s1, s2 =  s1_val, s2_val
        
