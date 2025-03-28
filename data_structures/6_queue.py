


from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')  # O(1)
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())   # O(1)
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty


## Below code is Linked list implementation of queue






class Node:

	def __init__(self, data):
		self.data = data
		self.next = None




class Queue:

	def __init__(self):
		self.front = self.rear = None

	def isEmpty(self):  # O(1)
		return self.front == None

	# Method to add an item to the queue
	def EnQueue(self, item):  # O(1)
		temp = Node(item)

		if self.rear == None:
			self.front = self.rear = temp
			return
		self.rear.next = temp
		self.rear = temp

	# Method to remove an item from queue
	def DeQueue(self):  # O(1)

		if self.isEmpty():
			return
		temp = self.front
		self.front = temp.next

		if(self.front == None):
			self.rear = None


# Driver Code
if __name__ == '__main__':
	q = Queue()
	q.EnQueue(10)
	q.EnQueue(20)
	q.DeQueue()
	q.DeQueue()
	q.EnQueue(30)
	q.EnQueue(40)
	q.EnQueue(50)
	q.DeQueue()
	print("Queue Front : " + str(q.front.data if q.front != None else -1))
	print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))







