class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
        self.prev = None
        
class Dl:
    def __init__(self):
        self.head =None
        self.tail =None
        
    def PushFront(self,key):   # O(1)
        node = Node(key)

        
        if self.head is None:
            self.head =node
            self.tail = node
            
            return
        node.next =self.head
        self.head.prev=node
        self.head =node
        
      
        

       
        
        
    def KeyFront(self):    # O(1)
        return self.head.key
        
        
    
    def PopFront(self):     #O(1)
        if self.head is None:
            print('empty')
            return
        
        remove = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        
        remove.next =None
        return remove.key
        
    
    def PushBack(self,key):     # O(1)
        node = Node(key)
        if self.head is None:
            self.head =node
            self.tail=node


        
        node.prev = self.tail

        self.tail.next=node
        
        self.tail =node
        
        
        
        
    
    def KeyBack(self):    # O(1)
        return self.tail.key
    
    def PopBack(self):      # O(1)
        
        removed = self.tail
        
        if self.tail is None:
            return None
        removed = self.tail
        
        self.tail =self.tail.prev
        if self.tail:
            self.tail.next = None
        removed.prev = None
        return removed.key
        



   
    
        
        
    def Print(self):
        if self.head is None:
            print('empty')
            return 
        
        itr = self.head
        
        llist =""
        
        while itr:
            llist+=str(itr.key)+'<->' if itr.next else str(itr.key)
            itr=itr.next
            
        print(llist)
        
        
if __name__=='__main__':
    b = "test"
    c = 5
    a = Dl()
    a.PushFront(2)
    a.Print()
    a.PushFront(22)
    a.Print()
  
    a.PushBack(69)
    a.Print()
    
    print(a.PopBack())
    a.Print()
    a.PushBack(456)
    a.Print()
    



