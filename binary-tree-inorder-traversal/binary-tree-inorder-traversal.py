# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        def inorder(root):
            if root:
                inorder(root.left)
                self.result.append(root.val)
                inorder(root.right)
        self.result = []
        inorder(root)
        return self.result