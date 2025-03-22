### BInary max tree
class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


    def Print(self):
        if self is not None:
            if self.left:
                self.left.Print()
            print(self.key)
            if self.right:
                self.right.Print()


    def GetMax(self):  # O(1)
        return self.key


    def Insert(self,key):
        if key<=self.key:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left = self.left.Insert(key)

        else:
            if self.right is None:
                self.right = TreeNode(key)

            else:
                self.right = self.right.Insert(key)


        pass

    def sift_up(self):
        pass


    def ExtractMax(self):
        pass

    def ShiftDown(self):
        pass

    def ChangePriority(self):
        pass

def InOrder(node):
    if node.left:
        InOrder(node.left)

    print(node.key)

    if node.right:
        InOrder(node.right)

if __name__=="__main__":
    root = TreeNode(42)
    root.left = TreeNode(29)
    root.right = TreeNode(18)
    root.left.left = TreeNode(14)
    root.left.right = TreeNode(7)
    root.left.left.left = TreeNode(11)
    root.right.right = TreeNode(18)
    root.right.right.left = TreeNode(12)
    root.right.right.right = TreeNode(7)
    # root.Print()

    # InOrder(root)
    root.Insert(31)
    InOrder(root)




    root.Print()
    print(root.GetMax())
    root.Insert(43)
    root.Print()
