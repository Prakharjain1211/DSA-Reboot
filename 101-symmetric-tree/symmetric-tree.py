# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helperfun(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return  self.helperfun(root1.left, root2.right) and self.helperfun(root1.right, root2.left)
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        root1,root2 = root.left , root.right
        if root is None:
           return True
        return self.helperfun(root.left,root.right)

        