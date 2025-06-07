# https://leetcode.com/problems/binary-tree-paths/description/
# [257] [Easy] Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, path, paths):
            if not root:
                return
            path.append(str(root.val))
            if not root.left and not root.right:
                paths.append("->".join(path))
            else:
                dfs(root.left, path, paths)
                dfs(root.right, path, paths)
            path.pop()
        paths = []
        dfs(root, [], paths)
        return paths
