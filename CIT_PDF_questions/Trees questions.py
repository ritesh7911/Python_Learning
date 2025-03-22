#1
class Tree:
    def __init__(self,key):
        self.key=key
        self.left =None
        self.right=None
T1 = Tree(5)
T2 = Tree(2)
T3 = Tree(10)
T4 = Tree(12)
T5 = Tree(14)

T1.left=T2
T1.right=T3
T3.left= T4
T3.right=T5


def height(root):
    if root is None:
        return -1

    left = height(root.left)
    right=height(root.right)

    return 1+max(left,right)
print(height(T1))


## 2 Number of elements or size of tree

def size(root):
    if root is None:
        return 0

    left = size(root.left)
    right=size(root.right)

    return 1+right+left
print(size(T1))


#3 program to delete tree of free up is nodes


# def delete(root):
#     root.left = None
#     root.right=None
#     root = None
#     return root

# above commented code will not work because it is not freeing up the memory only disconnecting root from its childs




def free_binary_tree(root):
    if root is None:
        return

    # First, free the nodes in the left subtree
    free_binary_tree(root.left)
    # Then, free the nodes in the right subtree
    free_binary_tree(root.right)

    # Finally, free the current node
    del root

# free_binary_tree(T1)
print(size(T1))


## 5. two identical trees or not


T1 = Tree(5)
T2 = Tree(2)
T3 = Tree(10)
T4 = Tree(12)
T5 = Tree(14)

T1.left=T2
T1.right=T3
T3.left= T4
T3.right=T5
T69 = Tree(90)
T11 = Tree(5)
T22 = Tree(2)
T33= Tree(10)
T44= Tree(12)
T55= Tree(14)
T11.left=T22
T11.right=T33
T33.left= T69
T33.right=T55



def compare_trees(t1,t2):
    if t1 is None and t2 is None:
        return True

    if t1.key==t2.key and compare_trees(t1.left,t2.left)and compare_trees(t1.right,t2.right):
        return True
    else:
        return False
print(compare_trees(T1,T11))


## 6. minimum in binary seach tree


def MinimumInBst(root):
    if root is None:
        return

    while root.left:

        root = root.left

    return root.key

print(MinimumInBst(T1))


##7 Maximum depth

##8 mirror copy of Tree


def Preorder(root):
    if root is None:
        return

    print(root.key)
    Preorder(root.left)
    Preorder(root.right)


Preorder(T1)


def MirrorTree(root):
    if root is None:
        return

    root.left,root.right=root.right,root.left

    root.left = MirrorTree(root.left)
    root.right = MirrorTree(root.right)

    return root


### what I am doing wrong was swaping values instead of nodes.

x=  MirrorTree(T1)

Preorder(x)

## 9 program of nth node in inorder traversal

##10. create copy of tree

def CopyTree(tree):
    if tree is None:
        return
    else:
        new_node = Tree(tree.key)
        new_node.left = CopyTree(tree.left)
        new_node.right = CopyTree(tree.right)

    return new_node

tx = CopyTree(T1)
print(compare_trees(T1,tx))

##11 bST or not
## below code is
# def isBST(root):
#     if root is None:
#         return
#
#
#
#     if root.left.key<root.key and root.key<root.right.key and isBST(root.left) and isBST(root.right):
#         return True
#     else:
#         return False

a = Tree(10)
b = Tree(5)
c = Tree(15)
a.left = b
a.right = c


def maxValueNode(root):
    if root is None:
        return float('-inf')  # Return negative infinity for an empty tree

    # Find the maximum value among the root and its children (if they exist)
    max_value = root.key

    if root.left is not None:
        max_value = max(max_value, maxValueNode(root.left))
    if root.right is not None:
        max_value = max(max_value, maxValueNode(root.right))

    return max_value


def minValueNode(root):
    if root is None:
        return float('+inf')  # Return negative infinity for an empty tree

    # Find the maximum value among the root and its children (if they exist)
    min_value = root.key

    if root.left is not None:
        min_value = min(min_value, minValueNode(root.left))
    if root.right is not None:
        min_value = min(min_value, minValueNode(root.right))

    return min_value


def ISBST(root):
    if root is None:
        return True
    lt_max = maxValueNode(root.left)
    rt_max = minValueNode(root.right)

    if lt_max<root.key and root.key<rt_max and ISBST(root.left) and ISBST(root.right):
        return True
    else:
        return False

print(ISBST(T1))