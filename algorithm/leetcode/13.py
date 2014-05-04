
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self,root):
        if root == None:
            return root
        stack = []
        ret = []
        stack.append(root)
        while stack:
            node =  stack.pop()
            left = node.left
            right = node.right
            ret.insert(0,node.val)
            if left != None:
                stack.append(left)
            if right != None:
                stack.append(right)


        return ret

def print_node_list(l):
    for node in l:
        print node,
    print 

def test_postorder():
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    root.left = n2
    root.right = n3

    n2.left = n4

    n3.left = n5
    n3.right = n6

    ss = Solution()
    l = ss.postorderTraversal(root)
    print_node_list(l)



if __name__ == '__main__':

    test_postorder()