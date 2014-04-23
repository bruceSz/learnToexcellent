class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self,root):
        ret = []
        stack = []
        if root == None:
            return ret
            
        stack.append(root)
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

        return ret
