class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self,head):
        if head == None:
            return False
        if head.next == None:
            return False
        if head.next == head:
            return True

        fast = head.next.next
        slow = head.next

        while fast != None and slow != None:
            if fast == slow:
                return True
            if fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next

        return False