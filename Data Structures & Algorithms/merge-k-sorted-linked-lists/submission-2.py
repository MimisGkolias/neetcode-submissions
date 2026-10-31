# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                if (i+1) > len(lists)-1:
                    mergedList.append(lists[i])
                    continue

                mergedList.append(self.mergeLists(lists[i], lists[i+1]))
            lists = mergedList
        return lists[0]



    
    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next















    #     while len(lists) > 1:
    #         merged_lists = []
    #         for i in range(0, len(lists), 2):
    #             if i + 1 >= len(lists):
    #                 merged_lists.append(lists[i])
    #                 continue

    #             merged = self.mergeTwoLists(lists[i], lists[i+1])
    #             merged_lists.append(merged)
                
    #         lists = merged_lists
    #     return lists[0]

    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     dummy = ListNode(0)
    #     current = dummy
        
    #     while list1 and list2:
    #         if list1.val <= list2.val:
    #             current.next = list1
    #             list1 = list1.next
    #         else:
    #             current.next = list2
    #             list2 = list2.next
    #         current = current.next
            
    #     if list1:
    #         current.next = list1
    #     elif list2:
    #         current.next = list2
            
    #     return dummy.next