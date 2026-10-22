# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        target = count - n

        if count == 1:
            return None

        dummy = ListNode(0, head)
        pointer = dummy
        for i in range(target):
            pointer = pointer.next
        tmp = pointer.next
        if pointer.next.next:
            pointer.next = pointer.next.next
        else:
            pointer.next = tmp.next
        tmp.next = None
    
        return dummy.next

