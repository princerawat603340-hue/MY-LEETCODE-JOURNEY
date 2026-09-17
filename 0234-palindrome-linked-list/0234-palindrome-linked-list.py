# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        newHead = None
        temp = head

        while temp:
            newNode = ListNode(temp.val)

            newNode.next = newHead
            newHead = newNode

            temp = temp.next

        temp=head
        temp2=newHead
        while temp2:
            if temp.val!=temp2.val:
                return False
            temp=temp.next
            temp2=temp2.next
        return True