# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, 1 + depth])
                stack.append([node.right, 1 + depth])
        return res













        # Recursive DFS
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Iterative BFS
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            depth += 1
        return depth

        # Iterative DFS
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, 1 + depth])
                stack.append([node.right, 1 + depth])
        return res


