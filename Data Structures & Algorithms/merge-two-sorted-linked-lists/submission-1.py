# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        ans = head
        if list1 == None and list2 == None:
            return None

        while (list1 != None or list2 != None):
            temp = ListNode()

            if list1 == None:
                temp.val = list2.val
                list2 = list2.next
            elif list2 == None:
                temp.val = list1.val
                list1 = list1.next
            elif list2.val > list1.val:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
            
            ans.next = temp
            ans = ans.next


        head = head.next
        return head

        
        
        