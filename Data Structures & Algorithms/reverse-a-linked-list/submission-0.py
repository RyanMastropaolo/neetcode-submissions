# Definition for singly-linked list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous