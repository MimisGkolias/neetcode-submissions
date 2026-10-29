# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1, pointer2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        pointer = dummy

        while pointer1 or pointer2 or carry:
            val1 = pointer1.val if pointer1 else 0
            val2 = pointer2.val if pointer2 else 0

            summ = val1 + val2 + carry

            digit = summ % 10
            carry = summ // 10

            new = ListNode(digit)
            pointer.next = new

            pointer = pointer.next
            if pointer1:
                pointer1 = pointer1.next
            if pointer2:
                pointer2 = pointer2.next

        return dummy.next

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        pointer1 = l1
        pointer2 = l2
        digit, carry = 0, 0
        dummy = curr = ListNode(0)

        while pointer1 or pointer2 or carry:
            val1 = pointer1.val if pointer1 else 0
            val2 = pointer2.val if pointer2 else 0
            total = carry + val1 + val2

            digit = total % 10
            carry = total // 10

            if pointer1:
                pointer1.val = digit
                curr.next = pointer1
            elif pointer2:
                pointer2.val = digit
                curr.next = pointer2
            else:
                curr.next = ListNode(digit)

            if pointer1:
                pointer1 = pointer1.next
            if pointer2:
                pointer2 = pointer2.next

            curr = curr.next
        return dummy.next
