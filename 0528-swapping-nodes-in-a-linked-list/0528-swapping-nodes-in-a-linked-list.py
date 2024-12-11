# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #we use 2 pointer approach
        #left pointer will be at the kth node from beginning
        #right pointer will be at the kth node from the end

        cur = head

        for i in range(k -1):
            cur = cur.next
        
        left = cur
        right = head

        while cur.next:
            cur = cur.next
            right = right.next
        
        left.val,right.val = right.val, left.val
        return head

            