## Q1. reverse LL

def reverseLL(head):
    if head is None:
        return None
    
    

    temp = None
    current = head

    while current:
        next = current.next
        current.next = temp
        temp = current
        current = next

    head = temp
    return head

    