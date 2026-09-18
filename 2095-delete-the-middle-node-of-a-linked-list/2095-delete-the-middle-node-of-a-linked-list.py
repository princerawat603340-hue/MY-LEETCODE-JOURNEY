# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        if slow.next is None:
            return None
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if slow.next is None:
            temp=head
            while temp.next != slow:
                temp=temp.next
            temp.next=None
            return head
        slow.val=slow.next.val
        slow.next=slow.next.next
        return head