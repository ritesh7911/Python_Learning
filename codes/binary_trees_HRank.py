class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    if root is None:
        return -1

    left_tree_height = height(root.left)
    right_tree_height = height(root.right)

    return  1+max(right_tree_height, left_tree_height)


tree = BinarySearchTree()

t = 1

arr = [3,5,2,1,4 ,6 ,7]
for i in range(t):
    tree.create(arr[i])

# print(height(tree.root))

## Level order traversal in Trees
from collections import deque

# q =deque()


# def BFS(root):
#     print(root.info)
#     if root is None:
#         return
#
#     queue = []
#
#     queue.append(root)
#
#     while (len(queue)>0):
#
#         print(queue[0].info)
#         cr = queue.pop(0)
#
#
#         if cr.left is not None:
#             print(cr.left.info)
#             queue.append(cr.left)
#         if cr.right is not None:
#             print(cr.right.info)
#             queue.append(cr.right)



def BFS1(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)
        print(current_node.info)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)





print(BFS1(tree.root))



