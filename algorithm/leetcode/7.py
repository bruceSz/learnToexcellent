class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity

        # the list here is actually the head 
        self.list = None
        self.len = 0
        #self.first = None
        self.tail = None

        self.map = {}

    def update_first(self,node):
        if node != None:
            pre_ = node.pre
            next_ = node.next

            if pre_ !=None:
                pre_.next = next_
    
            if next_!=None:    
                next_.pre = pre_
            # set node as the first node.
            node.pre = None
            node.next = self.list
            self.list.pre = node

            self.list = node

    def get(self,key):
        try:
            node = self.map[key]
        except :
            return -1
        self.update_first(node)
        return node.val

    def set(self,key,value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.update_first(node)
        else:
            if self.len == self.capacity:
                self.tail = self.tail.pre
                # in case the capacity is only 1
                if self.tail == None:
                    self.list = None
                else:
                    # although follow 1 step maybe useless,let's clean it anyway.
                    self.tail.next.pre = None
                    self.tail.next = None
            else:
                # i know this is ungly and not thread safe,
                # but, let's just ignore that.
                self.len+=1

            node = ListNode(value)
            self.map[key] = node

            node.next = self.list
            if self.list != None:
                self.list.pre = node
            self.list = node
            # if there is only on node here.
            if self.tail == None:
                self.tail = node



def main():
    lru = LRUCache(1)
    lru.set(2,1)
    
    print lru.get(2)
    lru.set(3,2)
    print lru.get(2)
    print lru.get(3)

if __name__ == '__main__':
    main()

