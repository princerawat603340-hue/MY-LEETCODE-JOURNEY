# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        length=0
        temp=head
        while temp:
            temp=temp.next
            length+=1
        def mergesort(head1,head2):
            i=head1
            j=head2
            
            head3=ListNode(0)
            tail=head3
            while i and j:
                if i.val>=j.val:
                    tail.next=j
                    j=j.next
                elif j.val>i.val:
                    tail.next=i
                    i=i.next
                tail=tail.next
            if i:
                tail.next=i
            if j:
                tail.next=j
            return head3.next

        def split(head,length):
            if length==1:
                return head

            jump=(length//2)-1
            temp=head
            for i in range(jump):
                temp=temp.next
            head2=temp.next
            temp.next=None
            left = split(head, jump+1)
            right = split(head2, length - jump-1)
            return mergesort(left, right)
        return split(head,length)

