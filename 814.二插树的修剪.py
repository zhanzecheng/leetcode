# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/17 下午5:29
# @Author  : zhanzecheng
# @File    : 814.二插树的修剪.py
# @Software: PyCharm
"""

# 这道题做的还是不错的，一遍AC

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return

        if not self.check(root):
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root

    def check(self, root):
        if not root:
            return False

        if root.val == 1:
            return True

        return self.check(root.left) or self.check(root.right)