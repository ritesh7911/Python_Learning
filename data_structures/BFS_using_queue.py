### Using simple python list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(tree):
    if tree is None:
        return

    q = []  # Using a list as a queue
    q.append(tree)

    while q:
        node = q.pop(0)  # Dequeue from the front of the list
        print(node.val, end=' ')

        if node.left:
            q.append(node.left) 
        if node.right:
            q.append(node.right)


# Creating the example binary tree
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

# Calling the level order traversal function
print("Level Order Traversal:")
level_order_traversal(tree)



from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def bfs(node):
    if node is None:
        return
    
    queue = deque([node])  # Initialize the queue with the root node
    
    while queue:
        current_node = queue.popleft()  # Remove the node from the front of the queue
        print(current_node.value)  # Process the current node
        
        # Add the children of the current node to the back of the queue
        queue.extend(current_node.children)

# Construct the tree (same as before)
root = TreeNode(1)
root.add_child(TreeNode(2))
root.add_child(TreeNode(3))
root.children[0].add_child(TreeNode(4))
root.children[0].add_child(TreeNode(5))
root.children[1].add_child(TreeNode(6))

# Perform BFS traversal
print("BFS traversal:")
bfs(root)

