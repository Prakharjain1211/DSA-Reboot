# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object): 

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def height(root):
            if root is None:
                return 0
            return max(height(root.left),height(root.right))+1
        
        def inorder(root):
            if root is None:
                return True

            d1 = height(root.left)
            d2 = height(root.right)

            if abs(d1 - d2) > 1:
                return False

            return inorder(root.left) and inorder(root.right)
        return inorder(root)
       