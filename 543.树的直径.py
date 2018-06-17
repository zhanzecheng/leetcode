# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 下午6:28
# @Author  : zhanzecheng
# @File    : 543.树的直径.py
# @Software: PyCharm
"""


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        depth = self.count_depth(root.left) + self.count_depth(root.right)
        return max(depth, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def count_depth(self, root):
        if not root:
            return 0

        depth = 1
        depth += max(self.count_depth(root.left), self.count_depth(root.right))
        return depth