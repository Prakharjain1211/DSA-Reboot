# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slwptr = head
        fastptr = head
        while(fastptr!=None and fastptr.next is not None):
            slwptr = slwptr.next
            fastptr = fastptr.next.next
        return slwptr

