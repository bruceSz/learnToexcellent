def quick_sort(l):
    if len(l)<=1:
        return l
    pivot = l.pop()
    ll = []
    lr = []
    for it in l:
        if it > pivot:
            lr.append(it)
        else:
            ll.append(it)

    ll = quick_sort(ll)
    lr = quick_sort(lr)
    ll.extend([pivot])
    ll.extend(lr)

    return ll

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def print_list(l):
    while l!=None:
        print l.val ,
        l=l.next

class Solution:
    def sortList(self,head):
        if head ==None:
            return head
        left = head.next
        pivot = head
        #pivot.next = None

        less = None
        big = None
        while left !=None:
            if left.val > pivot.val:
                tmp ,left= left,left.next
                tmp.next,big=big,tmp
            else:
                tmp,left = left,left.next
                tmp.next,less = less,tmp


        if less != None and less.next != None:
            less = self.sortList(less)

        if big!= None and  big.next!=None:
            big = self.sortList(big)

        if less == None:
            pivot.next = big
            return pivot
        else:
            tmp=less
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = pivot
            pivot.next = big
            return less

    def sortList2(self,head):
        if head == None or head.next == None:
            return head
        i=1;
        tmp = head
        while tmp.next != None:
            tmp=tmp.next
            i+=1
        half_i = 1
        tmp = head
        while half_i < i/2:
            tmp = tmp.next
            half_i +=1
            
        sec = tmp.next
        tmp.next = None

        l = self.sortList2(head)
        r = self.sortList2(sec)
        ret = None
        if l==None :
            return r
        if r == None:
            return l

        if l.val < r.val:
            ret = l
            l = l.next
        else:
            ret = r
            r = r.next

        tmp = ret
        while l!=None and r!=None:
            if l.val < r.val:
                tmp.next =  l
                l = l.next
                tmp = tmp.next
            else:
                tmp.next = r
                r = r.next
                tmp = tmp.next

        if l!=None:
            tmp.next = l
        if r!=None:
            tmp.next = r

        return ret
                
            



        
        

if __name__ == '__main__':
    #l = [-2,3,1,6,4]
    n1 = ListNode(-2)
    n2 = ListNode(3)
    n3 = ListNode(1)
    n4 = ListNode(6)
    n5 = ListNode(4)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5

    print_list(n1)

    solution = Solution()
    l=solution.sortList2(n1)
    print_list(l)


    #print quick_sort(l)
