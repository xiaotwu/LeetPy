# https://leetcode.com/problems/subtree-of-another-tree/description/
# [572] [Easy] Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return (s.val == t.val and isSametree(s.left, t.left) and isSametree(s.right, t.right))
        
        if not root:
            return False
        if isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
