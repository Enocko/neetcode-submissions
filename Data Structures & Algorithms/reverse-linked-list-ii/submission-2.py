# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        curr = head

        for i in range(left - 1):
            tail = curr
            curr = curr.next
        
        prev = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        tail.next.next = curr
        tail.next = prev
    
        return dummy.next

