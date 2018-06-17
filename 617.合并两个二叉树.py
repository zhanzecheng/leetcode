# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/16 下午6:41
# @Author  : zhanzecheng
# @File    : 617.合并两个二叉树.py
# @Software: PyCharm
"""

# 又是一种递归的方式

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if not t1 and not t2:
            return

        if not t1 and t2:
            root = t2
            return root

        if t1 and not t2:
            root = t1
            return root
        if t1 and t2:
            root = t1
            root.val += t2.val
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root