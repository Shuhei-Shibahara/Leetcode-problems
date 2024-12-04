class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy head and current node for the result linked list
        dummy_head = ListNode(0)
        current = dummy_head
        remainder = 0
        
        # Iterate while either l1 or l2 or remainder exists
        while l1 or l2 or remainder:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Sum the values along with any carry-over from the previous step
            total = val1 + val2 + remainder
            
            # Update the remainder (carry) for the next iteration
            remainder = total // 10
            current.next = ListNode(total % 10)
            
            # Move the current pointer to the new node
            current = current.next
            
            # Move l1 and l2 to their next nodes if available
            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next

