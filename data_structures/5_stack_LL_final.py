### implementation using list

## but it is slow and take a continous memory


## implementation using deque


from collections import deque

myStack = deque()

myStack.append('a')

myStack.append('b')
myStack.append('c')
print(myStack)

myStack

myStack.pop()
print(myStack)

myStack.pop()
print(myStack)
myStack.pop()
print(myStack)







class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
        
        
class Stack:
    def __init__(self):
        self.head =None
        
    def PushTop(self,key):
        node = Node(key)
        if self.head is None:
            self.head =node
            return
        
        node.next=self.head
        self.head =node
        
        
    def Top(self):
        print(self.head.key)
        return self.head.key
    
    
    def Pop(self):
        removed = self.head
        self.head =self.head.next
        return removed.key
    
    def isempty(self):
        if self.head is None:
            print('emmpty')
        return False
        
    def Print(self):
        if self.head is None:
            print('empty')
            return True
        
        itr = self.head
        
        llist =""
        
        while itr:
            llist+=str(itr.key)+'<--' if itr.next else str(itr.key)
            itr=itr.next
            
        print(llist)
        
if __name__=="__main__":
    l = Stack()
    l.PushTop(2)
    l.PushTop(3)
    l.Print()
    print(l.Top)
    l.PushTop(4)
    l.Print()