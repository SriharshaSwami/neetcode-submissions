# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        p=None
        c=slow.next
        while c:
            n=c.next
            c.next=p
            p=c
            c=n
        #p is head of the reversed half of the Linked list
        slow.next=None

        l1=head
        l2=p
        while l2:
            tmp1=l1.next
            tmp2=l2.next

            l1.next=l2
            l2.next=tmp1

            l1=tmp1
            l2=tmp2
        
        




