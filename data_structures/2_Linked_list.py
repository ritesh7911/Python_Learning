class Node:
    def __init__(self,key=None,next =None):
        self.key = key
        self.next = next
        
        
class LL:
    def __init__(self):
        self.head=None
        
    def PushFront(self,key):   #O(1)
        node = Node(key, self.head)

        self.head = node
        
    def Print(self):
        
        if self.head is None:
            print('Empty list')
            return None
        
        itr = self.head
        llist = ""
        
        while itr:
            llist += str(itr.key)+"->" if itr.next else str(itr.key)

            itr = itr.next

        print(llist)
            
            
    def TopFront(self):   #O(1)
        if self.head is None:
            print('Empty list')
            return None
        
        return self.head.key
    
    
    def PopFront(self):   # O(1)
#         node = Node(key)
        
        if self.head is None:
            print('Empty list')
            
        remove = self.head
        
        self.head = self.head.next
        
        remove.next = None
        
        return remove.key
    
    
    def PushBack(self,key):   # O(n)
        node = Node(key)
        
        if self.head is None:
            self.head = node
            return
            
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = node
        
        
        
    def PopBack(self):    ## O(n)
        
        
        if self.head is None:
            print('Nothing to return')
            
        itr = self.head
        
        if itr.next is None:
            return itr.key
            
        while itr.next:
            prev = itr
            itr = itr.next
            
        return prev.next.key
    
    
    def get_count(self):
        count = 0
        itr = self.head
        
        if itr is None:
            return 0
        
        while itr:
            count+=1
            
            itr = itr.next
            
        return count
    
    
    def Empty(self):  ##O(1)
        self.head =None
        
        
        
    def FindKey(self,key):   ## O(N)
        
#         node = Node(key)
        
        if self.head is None:
            print('Empty list')
            
        
        itr = self.head
        
        while itr:
            if itr.key==key:
                print('key is present')
                return itr.key
            
            itr = itr.next
            
            
        return 'Key is not present'
    
    
    # def AddAfter1(self,Exist_key, new_key):
    #     node = Node(new_key)


            
    def AddAfter(self,exit_key,new_key):   ## O(n)
        
        node = Node(new_key)
        
        if self.head is None:
            self.head = node
            
        itr = self.head
        
        while itr:
            if itr.key==exit_key:
                node.next = itr.next
                itr.next = node
                
            itr=itr.next
            
            
            
            
    def AddBefore(self, exit_key, new_key):   #O(n)
        node = Node(new_key)
        
        if self.head is None:
            print('Empty list')
            return
        
        if self.head.key == exit_key:
            node.next = self.head
            self.head = node
            return
        
        itr = self.head
        
        while itr.next:
            if itr.next.key == exit_key:
                node.next = itr.next
                itr.next = node
                return
            
            itr = itr.next
        
        print('Exit key not found in the list')


    def Reversing_linked_list(self):
        # temp = None
        # current = self.head
        #
        # while self.head is not None:
        #     temp = self.head.next

        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev





if __name__ =='__main__':
    l = LL()
    l.PushFront(2)
    l.PushFront(3)
    l.PushFront(33)

    l.Print()
    print(l.TopFront())
    l.Print()

    print(l.PopFront())
    l.Print()
    print(l.get_count())

    l.PushBack(456)
    l.Print()
    l.FindKey(2)



    # l.Print()
    l.AddBefore(456,222)
    l.Print()
    l.AddAfter(222,111)
    l.Reversing_linked_list()
    l.Print()


def print_linked_list(l):
    if l.head is None:
        return 'Nothing to print'

    current = l.head
    while current:
        print(current.key, end ='->')
        current = current.next
        if current is None:
            print('Null')



print_linked_list(l)


def lenght_of_linked_list(l):
    if l.head is None:
        return 'Nothing to print'

    c =1

    current = l.head
    while current.next:
        # print(current.key, end='->')

        current = current.next
        c+=1



    return c



print(lenght_of_linked_list(l))


# ## insert node at ith position
# def insert_node_at_ith_position(l,pos,value):
#     node1 = Node(value)
#
#
# #
#     if l.head is None:
#         l.head = node1
#         return l
# #
#     c =1
#     current = l.head
# #
#     while current.next:
#         c+=1
#         if c==pos:
#             node1.next = current.next
#             current.next  = node1
#         current = current.next
#
#     return current


# a = insert_node_at_ith_position(l,3,69)
#
# print_linked_list(a)


#
#         if c==pos:





