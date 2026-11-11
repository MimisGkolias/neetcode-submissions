# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        length = 0
        curr = curr.next
        while curr:
            length += 1
            curr = curr.next
        
        index = length - n
        curr = dummy
        for i in range(index):
            curr = curr.next
        
        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return dummy.next














        dummy = ListNode(0, head)
        left, right = dummy, head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next


