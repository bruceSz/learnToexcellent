class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:


    def reverse(self,head):
        if head == None or head.next == None:
            return head
        pre = head
        cur = head.next
        nex = head.next.next
        pre.next = None
        cur.next = pre

        while nex != None:
            pre = cur
            cur = nex
            nex= nex.next
            cur.next = pre
        return cur
    def merge(self,h1,h2):
        tmp1 = h1
        tmp2 = h2

        while tmp1 != None  and tmp2 != None:
            tmp = tmp1
            tmp1 = tmp1.next
            tmp.next = tmp2
            tmp = tmp2
            tmp2 =tmp2.next
            tmp.next = tmp1

        return h1

        

    def reorderList(self,head):
        if head == None or head.next == None:
            return head
        first = head.next
        second = head.next.next


        while second != None:
            
            if second.next == None:
                break
            first = first.next

            second = second.next.next
        
        second = first.next
        first.next = None
        second = self.reverse(second)

        head = self.merge(head,second)
        return head




def print_list(head):
    while head != None:
        print head.val,
        head = head.next
    print





if __name__ == '__main__':
    s = Solution()
    
    n1 =ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n3.next = n4

    n4.next = n5
    n5.next= n6

    print_list(n1)
    print_list(s.reorderList(n1))
