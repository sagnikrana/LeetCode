# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        self.low = low
        self.high = high
        self.children = []
        self.dfs(root)
        return self.sum
    
    
    def dfs(self, root):
        if root!= None:
            self.children = []
            
            if root.val >= self.low and root.val <= self.high:
                self.sum += root.val
            
            self.createChildren(root)

            for child in self.children:
                self.dfs(child)
                
    def createChildren(self, root):
        if root.left != None:
            self.children.append(root.left)
        if root.right != None:
            self.children.append(root.right)