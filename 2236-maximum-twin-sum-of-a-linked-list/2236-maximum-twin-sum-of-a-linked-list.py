# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #find the mid point by using slow and fast pointer
        #lets reverse the slow nodes and we will use the last slow to identify the right pointer

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = 0

        while slow:
            res = max(slow.val + prev.val, res)
            slow = slow.next
            prev = prev.next
        
        return res
