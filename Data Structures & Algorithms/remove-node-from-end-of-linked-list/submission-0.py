# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=q=head
        while n!=0:
            q=q.next
            n-=1
        while q and q.next:
            p=p.next
            q=q.next
        p.next=p.next.next
        return head