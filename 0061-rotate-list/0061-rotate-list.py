# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        length=0
        temp=head
        if not head:
            return None
        while temp.next:
            length+=1
            temp=temp.next
        last=temp
        if k%(length+1)==0:
            return head
        elif k>length+1:
            k=k%(length+1)
        rep=length-k+1
        temp=head
        while rep>1:
            temp=temp.next
            rep-=1
        last.next=head
        head=temp.next
        temp.next=None
        return head
        