# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        store = []
        res = []
        store.append(root)
        while len(store):
            node = store.pop()
            res.append(node.val)
            if node .right:
                store.append(node.right)
            if node.left:
                store.append(node.left)
        return res
            