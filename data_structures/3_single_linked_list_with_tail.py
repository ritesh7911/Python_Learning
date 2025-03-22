class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListWithTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def PushFront(self, data):  # O(1)
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
            
    def KeyFront(self):   #O(1)
        return self.head.data
    
    
    def PopFront(self):     # O(1)
        if self.head is None:
            print('Empty')
            return
        removed = self.head
        self.head = self.head.next
        removed.next =None
        return removed.data
    
    def PushBack(self,data):   # O(1)
        node = Node(data)
        if self.head is None:
            self.head =node
            self.tail=node
            return
        
        self.tail.next = node
        self.tail = node
            
            
    def KeyBack(self):   #O(1)
        return self.tail.key

    
    def PopBack(self):     # O(n)
        if self.head is None:
            print('Empty')
            return

        if self.head == self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            return removed.data

        itr = self.head
        while itr.next != self.tail:
            itr = itr.next

        removed = self.tail
        itr.next = None
        self.tail = itr
        return removed.data
    
    

        
        
        

    def display(self):
        # current = self.head
        # while current:
        #     print(current.data, end=" -> ")
        #     current = current.next
        # print("None")
        itr = self.head
        llist = ""

        while itr:
            llist += str(itr.data) + "->" if itr.next else str(itr.data)

            itr = itr.next

        print(llist)

# Example usage
linked_list = LinkedListWithTail()
linked_list.PushFront(1)
linked_list.PushFront(2)
linked_list.PushFront(3)
linked_list.display()
linked_list.display()
linked_list.PopBack()
linked_list.display()
linked_list.PopBack()
linked_list.display()
linked_list.PopBack()
linked_list.display()
linked_list.PopBack()
linked_list.display()