# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        res = []
        data = ''
        def dfs(root):
            if not root:
                res.append(None)
                return 
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        for val in res:
            data += str(val) + '#'
        return data
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        vals = data.split('#')[:-1]
        vals_iter = iter(vals)

        def reversedfs():
            val = next(vals_iter)
            
            if val == 'None':
                return None
                
            node = TreeNode(int(val))

            node.left = reversedfs()
            node.right = reversedfs()
            
            return node

        return reversedfs()
            
        


