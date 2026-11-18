# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        dummy = slow.next
        slow.next = None
        prev = None
        while dummy:
            nxt = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nxt
        
        # Merge the two lists
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        


















        
        # if not head or not head.next:
        #     return

        # slow, fast = head, head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # second = slow.next
        # prev = slow.next = None
        # while second:
        #     tmp = second.next
        #     second.next = prev
        #     prev = second
        #     second = tmp

        # first, second = head, prev
        # while second:
        #     tmp1, tmp2 = first.next, second.next
        #     first.next = second
        #     second.next = tmp1
        #     first, second = tmp1, tmp2


            