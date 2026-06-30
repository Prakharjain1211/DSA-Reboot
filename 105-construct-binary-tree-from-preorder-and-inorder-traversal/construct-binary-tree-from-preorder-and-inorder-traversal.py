# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def search(self,inorder,left,right,val):
        for i in range(left,right+1):
            if(inorder[i]==val):
                return i

    def helper(self, preorder, inorder, left, right):
        if left > right:
            return None
        root = TreeNode(preorder[self.preIdx])

        inIdx = self.search(inorder,left,right,preorder[self.preIdx])
        self.preIdx+=1

        root.left = self.helper(preorder, inorder, left, inIdx-1)
        root.right = self.helper(preorder, inorder, inIdx+1, right)

        return root


    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.preIdx = 0
        return self.helper(preorder, inorder,0,len(inorder)-1)
        