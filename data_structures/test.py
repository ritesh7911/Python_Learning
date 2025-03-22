# # # preorder traversal
# # # don't print node value that are on same level
# #
# #
# #
# #
# # Input :
# #         1
# #       /   \
# #     2       3
# #              \
# #              4
# #
# #
# # Output :1 2 4
# #
# #
# # Input :
# #                  1
# #                /   \
# #               2     3
# #              / \     \
# #             4   5     6
# #
# #
# # Output : 1 2 4
# #
# #
# # Input :
# #         1
# #       /   \
# #     2       3
# #       \
# #         4
# #           \
# #             5
# #              \
# #                6
# #
# #
# # Output :1 2 4 5 6
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def InorderTraversal(node):
#     if node:
#         InorderTraversal(node.left)
#         print(node.val)
#
#         InorderTraversal(node.right)
#
#
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(6)
#
#
# # InorderTraversal(root)
#
#
#
# def left_view(root):
#     if not root:
#         return []
#
#     result = []
#     queue = [root]
#
#
#     while queue:
#         level_size = len(queue)
#
#
#
#
#         for i in range(level_size):
#             node = queue.pop(0)
#             # print(queue)
#             if i == 0:
#                 result.append(node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#     return result
#
# # Example usage
# # Constructing a sample binary tree
# # root = TreeNode(1)
# # root.left = TreeNode(2)
# # root.right = TreeNode(3)
# # root.left.right = TreeNode(4)
# # root.right.left = TreeNode(5)
# # root.right.right = TreeNode(6)
#
# result = left_view(root)
# print(result)  # Output: [1, 2, 4]


# l = [2,1,1,2]
# stx = l[1]
# sty = l[3]
# inx = 2+stx
# iny = 2+sty





