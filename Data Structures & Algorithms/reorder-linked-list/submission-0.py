# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p=q=head
        while q:
            p=p.next
            q=q.next.next
        c=p
        p=None
        while c:
            n=c.next
            c.next=p
            c=n
            p=c
        p=head
        q=p.next
        while c:
            p.next=c
            c=c.next
            p=q
            q=q.next
        return head

