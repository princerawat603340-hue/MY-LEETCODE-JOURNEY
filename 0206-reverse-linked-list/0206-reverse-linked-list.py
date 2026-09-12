# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        new_link=None
        while temp is not None:
            new_node=ListNode(temp.val)
            new_node.next=new_link
            new_link=new_node
            temp=temp.next
        return new_link