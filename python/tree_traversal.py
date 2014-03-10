# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def r_preorderTraversal(root,L):
        L.append(root.val)
        if root.left is not None:
            r_preorderTraversal(root.left,L)
        if root.right is not None:
            r_preorderTraversal(root.right,L)
    
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        L=[]
        r_preorderTraversal(root,L)
        return L
