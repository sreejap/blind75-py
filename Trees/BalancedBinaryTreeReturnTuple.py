# https://leetcode.com/problems/balanced-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedHelper(self, root: Optional[TreeNode]) -> (bool, int):
        if not root:
            return True,0
        
        leftBalanced, leftHeight = self.isBalancedHelper (root.left)
        if not leftBalanced:
            return False, leftHeight

        rightBalanced, rightHeight = self.isBalancedHelper (root.right)
        if not rightBalanced:
            return False, rightHeight
        
        return (abs(leftHeight - rightHeight) < 2 , 1 + max(leftHeight,rightHeight))        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[0]        
