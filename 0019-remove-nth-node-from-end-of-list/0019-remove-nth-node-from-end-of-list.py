# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count=0
        temp=head
        if temp.next is None:
            return None

        while temp:
            count+=1
            temp=temp.next
        rep=count-n
        temp=head
        if n==1:
            rep=rep-1
            while rep>0:
                temp=temp.next
                rep-=1
            temp.next=None
            return head

        
        while rep>0:
            temp=temp.next
            rep-=1
        temp.val=temp.next.val
        temp.next=temp.next.next
        return head