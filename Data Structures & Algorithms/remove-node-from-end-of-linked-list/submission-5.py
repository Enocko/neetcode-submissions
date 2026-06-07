# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy

        curr = head
        while curr and n > 0:
            curr = curr.next
            n -= 1
        
        while curr:
            tail = tail.next
            curr = curr.next


        tail.next = tail.next.next
        return dummy.next


"""
curr = 3 -> 4
tail = 1 -> 2

"""