# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        counter = 1

        while True:
            level_size = len(queue) 
            if level_size == 0:
                return result
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()  
                current_level.append(node.val)                
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if counter % 2 ==0:
                result.append(current_level[::-1])  
            else:
                result.append(current_level)  
            counter +=1

        return result
        