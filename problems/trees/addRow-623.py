# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addHelper(self, root, v, d, curr_d):
        if root == None:
            return
        if curr_d == d - 1:
            print root.val
            node_t_l = TreeNode(v)
            node_t_l.left = root.left
            node_t_r = TreeNode(v)
            node_t_r.right = root.right
            root.left = node_t_l
            root.right = node_t_r
            return

        self.addHelper(root.left, v, d, curr_d + 1)
        self.addHelper(root.right, v, d, curr_d + 1)

    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node_t = TreeNode(v)
            node_t.left = root
            return node_t
        self.addHelper(root, v, d, 1)
        return root
