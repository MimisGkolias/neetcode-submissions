# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Optimized solution to pass the tests
        inorder_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0
        
        def helper(in_left, in_right):
            nonlocal pre_idx
            if in_left > in_right:
                return None
            
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            mid = inorder_map[root_val]
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            
            return root
        
        return helper(0, len(inorder) - 1)



        # Neetoce solution
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root