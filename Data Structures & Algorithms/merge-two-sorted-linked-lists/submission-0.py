# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode(0)
        p=list1
        q=list2
        r=list3
        while p and q:
            if p.val<=q.val:
                r.next=ListNode(p.val)
                p=p.next
                r=r.next
            else:
                r.next=ListNode(q.val)
                q=q.next
                r=r.next
        if p:
            while p:
                r.next=ListNode(p.val)
                r=r.next
                p=p.next
        if q:
            while q:
                r.next=ListNode(q.val)
                r=r.next
                q=q.next
        return list3.next

