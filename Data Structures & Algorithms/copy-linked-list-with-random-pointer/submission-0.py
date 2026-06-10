"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={ None : None }
        old=head
        while old:
            oldToCopy[old] = Node(old.val)
            old = old.next
        
        old = head
        while old:
            oldToCopy[old].next = oldToCopy[old.next]
            oldToCopy[old].random = oldToCopy[old.random]
            old = old.next

        return oldToCopy[head]
        