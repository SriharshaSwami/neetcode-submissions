# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        leftpre=dummy
        curr=head
        for i in range(left-1):
            leftpre=pre.next
            curr=curr.next
        prev=None
        for i in range(right-left+1):
            n=curr.next
            curr.next=p
            prev,curr=curr,n
        leftprev.next.next=curr
        leftprev.next=prev
        return dummy.next
    
        