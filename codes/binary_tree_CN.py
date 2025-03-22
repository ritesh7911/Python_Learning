class Tree:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right  =None


t1 = Tree(5)

t2 = Tree(2)

t3 = Tree(10)

t4 = Tree(11)

t5 = Tree(12)

t1.left = t2
t1.right = t3

t3.left = t4

t3.right = t5

def PrintTree(Tree):
    if Tree is None:
        print('Empty')
        return
    q = []
    q.append(Tree)

    while len(q)>0:
        nodes = q.pop(0)
        print(nodes.data, end = ' ')

        if nodes.left is not None:
            q.append(nodes.left)

        if nodes.right is not None:
            q.append(nodes.right)


PrintTree(t1)


## number of Nodes in a binary tree

def size_of_tree(root):
    if root is None:
        return 0

    left_tree = size_of_tree(root.left)
    right_tree = size_of_tree(root.right)

    return 1+left_tree+right_tree


def sum_of_nodes(Tree):
    if Tree is None:
        return

    q = []
    results =[]
    q.append(Tree)

    while len(q)>0:
        nodes = q.pop(0)
        results.append(nodes.data)

        if nodes.left is not None:
            q.append(nodes.left)

        if nodes.right is not None:
            q.append(nodes.right)

    print(results)

    return sum(results)






print(size_of_tree(t1))

print(sum_of_nodes(t1))


### print nodes with the largest data


def maximum_nodes(Tree):
    if Tree is None:
        return

    q = []
    results =[]
    q.append(Tree)

    while len(q)>0:
        nodes = q.pop(0)
        results.append(nodes.data)

        if nodes.left is not None:
            q.append(nodes.left)

        if nodes.right is not None:
            q.append(nodes.right)

    # print(results)

    return max(results)

print(maximum_nodes(t1))


## number of nodes greater than particular value


## height of tree

def height_of_tree(root):
    if root is None:
        return -1

    left_tree = height_of_tree(root.left)
    right_tree = height_of_tree(root.right)

    return 1 +max(left_tree,right_tree)


print(height_of_tree(t1))


## number of leaf nodes


def no_of_leaf_nodes(root):
    if root is None:
        return 0

    if (root.left is None) and (root.right is None) :
        return 1


    else :
        return no_of_leaf_nodes(root.left) + no_of_leaf_nodes(root.right)



print(no_of_leaf_nodes(t1))


## print node at depth k

def Print_node_at_depth_k(root,k):
    if root is None:
        return

    if k == 0:
        print(root.data, end = ' ')

    else:
        Print_node_at_depth_k(root.left, k-1)
        Print_node_at_depth_k(root.right, k-1)




Print_node_at_depth_k(t1,k=2)



## remove_leaf_nodes

def remove_leaf_nodes(root):
    if root is None:
        return None

    if (root.left is None) and (root.right is None):
        return None

    root.left = remove_leaf_nodes(root.left)
    root.right = remove_leaf_nodes(root.right)

    return root

x = remove_leaf_nodes(t1)

PrintTree(x)




