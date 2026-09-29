# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head=ListNode(0)
        var=head
        temp1=list1
        temp2=list2
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                newnode=ListNode(temp1.val)
                var.next=newnode
                var=var.next  
                temp1=temp1.next
            else:
                newnode=ListNode(temp2.val)
                var.next=newnode
                var=var.next 
                temp2=temp2.next
        while temp1:
            var.next=temp1
            break
        while temp2:
            var.next=temp2
            break
        return head.next