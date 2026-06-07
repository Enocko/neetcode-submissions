# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp    
    
        h1, h2 = head, prev
        while h2:
            tmp1, tmp2 = h1.next, h2.next
            h1.next = h2
            h2.next = tmp1
            h1, h2 = tmp1, tmp2

"""
slow  = 4
fast = 8

prev = 8 -> 6

h1 = 2 -> 4 -> 6 -> 8
h2 = 8 -> 6

t1, t2 = 4, 6

h1
"""