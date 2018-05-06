# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        s = [root]
        res = []
        while len(s) != 0:
            node = s.pop()
            if node != None:
                res.append(node.val)
                s.append(node.right)
                s.append(node.left)

        return res
