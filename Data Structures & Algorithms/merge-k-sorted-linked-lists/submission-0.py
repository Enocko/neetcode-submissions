# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]

        m = len(lists) // 2
        left = self.mergeKLists(lists[:m])
        right = self.mergeKLists(lists[m:])
        return self.merge(left, right)
    

    def merge(self, l, r):
        dummy = ListNode()
        tail = dummy

        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        
        tail.next = l or r
        return dummy.next

