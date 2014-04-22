class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self,head):
        if head == None:
            return None
        if head.next == None:
            return None
        if head.next == head:
            return head

        fast = head.next.next
        slow = head.next

        while fast != None and slow != None:
            if fast == slow:
                flag = True
                step = 1
                slow=slow.next
                while slow!=fast:
                    slow=slow.next
                    step +=1

                front=rear=head
                while step!=0:
                    step-=1
                    front=front.next

                while front!=rear:
                    front = front.next
                    rear = rear.next

                return front
                
                
            if fast.next == None:
                return None
            fast = fast.next.next
            slow = slow.next
        # if exist, won't pass through while loop at all.
            return None
