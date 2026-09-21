# Definition for singly-linked list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head  # Node 0

        while current_node:
            next_node = current_node.next # stores current_node.next pointer to next_node

            current_node.next = previous_node # points current_node.next pointer to previous_node

            previous_node = current_node  # previous_node updated to current_node
            current_node = next_node  # current_node updated to next_node
        
        return previous_node