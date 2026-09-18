# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointer1=headA
        pointer2=headB
        while pointer1!=pointer2:
            if pointer1 is None:
                pointer1=headB
            else:
                pointer1=pointer1.next
            if pointer2 is None:
                pointer2=headA
            else:
                pointer2=pointer2.next
        return pointer1