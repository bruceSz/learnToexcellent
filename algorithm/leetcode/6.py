
def print_list(l):
    while l!=None:
        print l.val ,
        l=l.next

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self,head):
        if head == None:
            return head
        left = head.next
        head.next = None

        left = self.insertionSortList(left)
        #print 'head is:'
        #print head.val
        #print 'left is:'
        #print_list(left)
        #print 
        if left==None:
            return head
        if head.val <= left.val:
            head.next = left
            return head
        else:
            ret = left
            while left.next !=None:
                if head.val <= left.next.val:
                    head.next=left.next
                    left.next = head
                    return left
                left = left.next

            left.next = head
            return ret

            
        # head.val is the biggest. hence jump out of while loop

    def insertionSortList2(self,head):
        if head == None or head.next == None:
            return head
        next_ = head.next.next
        pivot = head.next
        head.next = None
        pivot.next = None

        while True:
            if pivot.val <=head.val:
                pivot.next = head
                head = pivot
            else:
                tmp_h = head
                while tmp_h.next != None:
                    if pivot.val <= tmp_h.next.val:
                        pivot.next = tmp_h.next
                        tmp_h.next = pivot
                        break
                    tmp_h= tmp_h.next
                if tmp_h.next == None:
                    tmp_h.next=pivot

            pivot = next_
            if next_ == None:
                break
            next_=next_.next
            pivot.next = None
        return head


    def insertionSortList3(self,head):
        if head == None or head.next == None:
            return head
        else:
            cur = head.next
            while cur != None:

                tmp_h = head
                
                while tmp_h.val < cur.val:
                    tmp_h = tmp_h.next



                pre_val = cur.val
                #print '\nhaha',pre_val
                while tmp_h.next != cur.next:

                    tmp_val = tmp_h.val
                    tmp_h.val = pre_val
                    pre_val = tmp_val
                    tmp_h = tmp_h.next
                tmp_h.val=pre_val

                cur = cur.next

        return head









if __name__ =='__main__':
    
    #n1 = ListNode(-2)
    #n2 = ListNode(3)
    #n3 = ListNode(1)
    #n4 = ListNode(6)
    #n5 = ListNode(4)
    #n1.next=n2
    #n2.next=n3
    #n3.next=n4
    #n4.next=n5
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(1)
    n1.next = n2
    n2.next = n3

    print_list(n1)

    solution = Solution()
    l=solution.insertionSortList2(n1)
    print_list(l)

