# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  
        dummy = ListNode(0, head)
        current = head
        length = 0
        

        while current:
            length += 1
            current = current.next

        carry = dummy
        for i in range(0, length, k):
            old_first = carry.next
            curr = old_first
            prev = None
            

            if (length - i) < k:
                break
            else:
                for _ in range(k):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                carry.next = prev
                old_first.next = curr
                carry = old_first


        return dummy.next

