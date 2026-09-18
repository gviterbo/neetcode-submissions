# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        if head == None:
            return None
        ans.next = None
        ans.val = head.val
        head = head.next
        while(head != None):
            temp = ListNode()
            temp.next = ans
            temp.val = head.val
            head = head.next
            ans = temp

        return ans


        